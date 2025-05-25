import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Circle")

score = 0
radius = 50


def random_pos():
    return random.randint(radius, WIDTH - radius), random.randint(radius, HEIGHT - radius)


circle_pos = random_pos()

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 200, 255), circle_pos, radius)
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if (mx - circle_pos[0]) ** 2 + (my - circle_pos[1]) ** 2 <= radius ** 2:
                score += 1
                circle_pos = random_pos()
pygame.quit()
sys.exit()
