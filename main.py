import pygame
import random

pygame.init()   # Start pygame


WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


#Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake And Apple")

# Characters
snake =[(100,100), (80,100), (60,100)]
snake_dir = (GRID_SIZE,0)
apple = (random.randint(0, WIDTH//GRID_SIZE-1)*GRID_SIZE, random.randint(0, HEIGHT//GRID_SIZE-1)*GRID_SIZE)




#Variables

clock = pygame.time.Clock()
running = True
score = 0
speed = 7

#Main engine
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.quit:
            running =False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)


    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)
    snake.insert(0, new_head)

    if new_head == apple:
        score += 1
        apple = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
                 random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
        if score % 3 == 0:
            speed += 2
    else:
        snake.pop()


# Collision
    if (new_head in snake[1:]):
        running = False

    pygame.draw.rect(screen, RED, (apple[0], apple[1], GRID_SIZE, GRID_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    pygame.display.update()
    clock.tick(speed)











pygame.quit()
print(f"Your score is{score}")