import sys
import pygame
import random
from pygame.math import Vector2
from MainClass import Main

pygame.mixer.pre_init(44100, -16, 2, 512)
# Init all pygame component
pygame.init()

# Define a certain amount and size of cell to simulate a grid
cell_size = 40
cell_number = 20


# Define the display surface
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

# Run a max speed clock
FramesPerSecond = pygame.time.Clock()

main_game = Main(cell_number, cell_size, screen)

# Create a new event to trigger the moving function
SCREEN_UPDATE = pygame.USEREVENT
# Create a timer to activate the event every few milliseconds
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    # Get all event that are happening in the game
    for event in pygame.event.get():
        # If the event is a click on the red x mark
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        # Get every event from the user that are key down related
        if event.type == pygame.KEYDOWN:
            # Go up if the key 'UP'/'W'/'Z' is pressed
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_z:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            # Go down if the key 'DOWN'/'S' is pressed
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            # Go right if the key 'RIGHT'/'D' is pressed
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            # Go left if the key 'LEFT'/'A'/'Q' is pressed
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_q:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    # Apply some color on the display surface
    screen.fill((175, 215, 70))

    # Add the snake and fruit on the screen
    main_game.draw_elements()

    # Draw all our elements
    pygame.display.update()

    # Limit the speed of execution to 60 frames per second
    FramesPerSecond.tick(60)
