import pygame
import random
import sys
import time

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Reaction Game")
font = pygame.font.SysFont(None, 72)
score_font = pygame.font.SysFont(None, 40)  # Font for score display

keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
key_names = {pygame.K_LEFT: "LEFT", pygame.K_RIGHT: "RIGHT", pygame.K_UP: "UP", pygame.K_DOWN: "DOWN"}


def new_arrow():
    return random.choice(keys)


arrow = new_arrow()
start_time = time.time()
score = 0

running = True
while running:
    screen.fill((255, 255, 255))
    # Draw the arrow text
    text = font.render(key_names[arrow], True, (0, 0, 0))
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    # Draw the score
    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == arrow:
                reaction = time.time() - start_time
                score += 1
                print(f"Reaction Time: {reaction:.2f}s | Score: {score}")
                arrow = new_arrow()
                start_time = time.time()
pygame.quit()
sys.exit()
