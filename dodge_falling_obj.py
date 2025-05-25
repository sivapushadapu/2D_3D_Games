import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")

player_width = 60
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 0.9

object_width = 40
object_height = 40
object_x = random.randint(0, WIDTH-object_width)
object_y = 0
object_speed = 0.7

lives = 3
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill((220,220,220))
    pygame.draw.rect(screen, (0,0,255), (player_x, player_y, player_width, 30))
    pygame.draw.rect(screen, (255,0,0), (object_x, object_y, object_width, object_height))
    lives_text = font.render(f"Lives: {lives}", True, (0,0,0))
    screen.blit(lives_text, (10, 10))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    object_y += object_speed
    if object_y > HEIGHT:
        object_y = 0
        object_x = random.randint(0, WIDTH-object_width)

    # Collision detection
    if (player_y < object_y+object_height < player_y+30) and (player_x < object_x+object_width and player_x+player_width > object_x):
        lives -= 1
        object_y = 0
        object_x = random.randint(0, WIDTH-object_width)
        if lives == 0:
            print("Game Over!")
            running = False
pygame.quit()
sys.exit()
