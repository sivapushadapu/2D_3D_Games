import pygame
import random
import time
import sys

# --- Game Config ---
ROWS, COLS = 4, 5  # 10 pairs (20 cards)
CARD_SIZE = 100
GAP = 20
WIDTH = COLS * CARD_SIZE + (COLS + 1) * GAP
HEIGHT = ROWS * CARD_SIZE + (ROWS + 1) * GAP + 60
FPS = 60

# --- Colors ---
BG_COLOR = (30, 30, 60)
CARD_BACK = (80, 80, 120)
CARD_COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 128, 0),  # Orange
    (0, 128, 255),  # Light Blue
    (128, 0, 128),  # Purple
    (0, 128, 128),  # Teal
] * 2  # Duplicate for pairs

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Matching Game")
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# --- Card Setup ---
class Card:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.flipped = False
        self.matched = False
        self.animating = False
        self.flip_progress = 0  # 0 = not animating, 1 = fully flipped
        self.flip_to = False  # Target state after animation

    def rect(self):
        return pygame.Rect(self.x, self.y, CARD_SIZE, CARD_SIZE)

    def draw(self, surf):
        # Calculate width for flip animation
        if self.animating:
            scale = abs(1 - 2 * self.flip_progress)  # 1->0->1
        else:
            scale = 1

        w = max(1, int(CARD_SIZE * scale))
        rect = pygame.Rect(self.x + (CARD_SIZE - w) // 2, self.y, w, CARD_SIZE)

        if self.flipped or (self.animating and self.flip_progress > 0.5):
            color = self.color
        else:
            color = CARD_BACK

        pygame.draw.rect(surf, color, rect)
        pygame.draw.rect(surf, (200, 200, 200), rect, 2)

    def start_flip(self, to_flipped):
        self.animating = True
        self.flip_progress = 0
        self.flip_to = to_flipped

    def update(self):
        if self.animating:
            self.flip_progress += 0.12  # Animation speed
            if self.flip_progress >= 1:
                self.flip_progress = 1
                self.animating = False
                self.flipped = self.flip_to


def create_board():
    colors = CARD_COLORS[:]
    random.shuffle(colors)
    cards = []
    for row in range(ROWS):
        row_cards = []
        for col in range(COLS):
            x = GAP + col * (CARD_SIZE + GAP)
            y = GAP + row * (CARD_SIZE + GAP) + 60
            color = colors.pop()
            row_cards.append(Card(x, y, color))
        cards.append(row_cards)
    return cards


def reset_game():
    global cards, first, second, flipping, flip_time, moves, matches, start_time, game_over, elapsed
    cards = create_board()
    first = None
    second = None
    flipping = False
    flip_time = 0
    moves = 0
    matches = 0
    start_time = time.time()
    elapsed = 0
    game_over = False


# Initialize game variables
reset_game()

# --- Main Loop ---
running = True
while running:
    screen.fill(BG_COLOR)

    if not game_over:
        elapsed = int(time.time() - start_time)

    # Draw and update cards
    for row in cards:
        for card in row:
            card.draw(screen)
            card.update()

    # Draw info
    moves_text = font.render(f"Moves: {moves}", True, (255, 255, 255))
    time_text = font.render(f"Time: {elapsed}s", True, (255, 255, 255))
    screen.blit(moves_text, (20, 10))
    screen.blit(time_text, (WIDTH - 150, 10))

    # Check for win condition
    if matches == ROWS * COLS // 2 and not game_over:
        game_over = True

    # Display win message if game over
    if game_over:
        win_text = font.render("You Win! Press R to Restart or ESC to Quit", True, (0, 255, 0))
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, 40))

    pygame.display.flip()
    clock.tick(FPS)

    # Handle flipping back unmatched cards after delay
    if flipping and time.time() - flip_time > 1 and not first.animating and not second.animating:
        if first.color == second.color:
            first.matched = True
            second.matched = True
            matches += 1
        else:
            first.start_flip(False)
            second.start_flip(False)
        first = None
        second = None
        flipping = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not flipping and not game_over:
            mx, my = event.pos
            for row in cards:
                for card in row:
                    if card.rect().collidepoint(mx, my) and not card.flipped and not card.matched and not card.animating:
                        card.start_flip(True)
                        if not first:
                            first = card
                        elif not second and card != first:
                            second = card
                            moves += 1
                            flipping = True
                            flip_time = time.time()

        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset_game()
            elif event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
sys.exit()
