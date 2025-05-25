import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 10
PAD_WIDTH, PAD_HEIGHT = 8, 80

ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [random.choice([-4, 4]), random.choice([-3, 3])]
paddle1_pos = HEIGHT // 2 - PAD_HEIGHT // 2  # Left paddle vertical position
paddle2_pos = HEIGHT // 2 - PAD_HEIGHT // 2  # Right paddle vertical position
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

font = pygame.font.SysFont(None, 36)

# Paddle movement speed
PADDLE_SPEED = 6


def draw():
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, (0, paddle1_pos, PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PAD_WIDTH, paddle2_pos, PAD_WIDTH, PAD_HEIGHT))

    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)

    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 40, 10))
    pygame.display.flip()


running = True
clock = pygame.time.Clock()

while running:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Left paddle controls
            if event.key == pygame.K_w:
                paddle1_vel = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                paddle1_vel = PADDLE_SPEED
            # Right paddle controls
            elif event.key == pygame.K_UP:
                paddle2_vel = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                paddle2_vel = PADDLE_SPEED
        elif event.type == pygame.KEYUP:

            if event.key in [pygame.K_w, pygame.K_s]:
                paddle1_vel = 0

            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                paddle2_vel = 0

    # Update paddle positions with boundary checks
    paddle1_pos += paddle1_vel
    paddle1_pos = max(0, min(HEIGHT - PAD_HEIGHT, paddle1_pos))

    paddle2_pos += paddle2_vel
    paddle2_pos = max(0, min(HEIGHT - PAD_HEIGHT, paddle2_pos))

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Ball collision with top/bottom walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # Ball collision with left paddle
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
        else:
            score2 += 1
            ball_pos = [WIDTH // 2, HEIGHT // 2]
            ball_vel = [random.choice([-4, 4]), random.choice([-3, 3])]

    # Ball collision with right paddle
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if paddle2_pos <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
        else:
            score1 += 1
            ball_pos = [WIDTH // 2, HEIGHT // 2]
            ball_vel = [random.choice([-4, 4]), random.choice([-3, 3])]
    clock.tick(60)
pygame.quit()
sys.exit()
