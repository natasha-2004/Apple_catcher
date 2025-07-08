import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🍎 Catch the Falling Fruit")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

# Basket
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 7

# Apple
apple_radius = 15
apple_x = random.randint(apple_radius, WIDTH - apple_radius)
apple_y = 0
apple_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move apple
    apple_y += apple_speed
    if apple_y > HEIGHT:
        apple_y = 0
        apple_x = random.randint(apple_radius, WIDTH - apple_radius)

    # Check collision
    if (basket_y < apple_y + apple_radius < basket_y + basket_height and
            basket_x < apple_x < basket_x + basket_width):
        score += 1
        apple_y = 0
        apple_x = random.randint(apple_radius, WIDTH - apple_radius)

    # Draw apple
    pygame.draw.circle(screen, RED, (apple_x, apple_y), apple_radius)

    # Draw basket
    pygame.draw.rect(screen, BROWN, (basket_x, basket_y, basket_width, basket_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
