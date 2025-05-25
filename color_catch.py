import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Catch Game")

# Game settings
BUCKET_WIDTH, BUCKET_HEIGHT = 100, 30
BUCKET_SPEED = 7
FALLING_SPEED = 7
FALLING_SIZE = 50

# Initialize game elements
bucket_x = WIDTH // 2 - BUCKET_WIDTH // 2
bucket_y = HEIGHT - 60
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
target_color = random.choice(colors)
falling_color = random.choice(colors)
falling_x = random.randint(0, WIDTH - FALLING_SIZE)
falling_y = 0
score = 0

# Fonts
font = pygame.font.SysFont(None, 36)
target_font = pygame.font.SysFont(None, 24)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))
    dt = clock.tick(60)  # Limit to 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bucket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bucket_x > 0:
        bucket_x -= BUCKET_SPEED
    if keys[pygame.K_RIGHT] and bucket_x < WIDTH - BUCKET_WIDTH:
        bucket_x += BUCKET_SPEED

    # Falling block movement
    falling_y += FALLING_SPEED
    if falling_y > HEIGHT:
        falling_y = 0
        falling_x = random.randint(0, WIDTH - FALLING_SIZE)
        falling_color = random.choice(colors)

    # Collision detection using Rect
    bucket_rect = pygame.Rect(bucket_x, bucket_y, BUCKET_WIDTH, BUCKET_HEIGHT)
    falling_rect = pygame.Rect(falling_x, falling_y, FALLING_SIZE, FALLING_SIZE)

    if bucket_rect.colliderect(falling_rect):
        if falling_color == target_color:
            score += 1
        else:
            score = max(0, score - 1)  # Prevent negative scores
        falling_y = 0
        falling_x = random.randint(0, WIDTH - FALLING_SIZE)
        falling_color = random.choice(colors)

    # Drawing
    # Target color display
    pygame.draw.rect(screen, target_color, (20, 20, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (20, 20, 50, 50), 2)
    target_text = target_font.render("Target Color:", True, (0, 0, 0))
    screen.blit(target_text, (20, 80))

    # Bucket
    pygame.draw.rect(screen, (128, 128, 128), bucket_rect)

    # Falling block
    pygame.draw.rect(screen, falling_color, falling_rect)

    # Score display
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (WIDTH - 150, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()
