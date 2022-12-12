import sys
import pygame
import random
from pygame.math import Vector2

# Create a Fruit class which generate a random position with Vector to a better manipulation of its coord, also add a method to create and draw the fruit on the map
class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

class Snake:
    def __init__(self):
        # Represent the length and position of our snake
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        # Represent the moving direction for the snake
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            # Create a rectangle from the pos and draw the rectangle
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)

    def move_snake(self):
        # Copy the body properties except the last one
        body_copy = self.body[:-1]
        # Insert a new item right at the start for the new position of the head
        body_copy.insert(0, body_copy[0] + self.direction)
        # Assign the new position to the self property
        self.body = body_copy[:]



# Init all pygame component
pygame.init()

# Define a certain amount and size of cell to simulate a grid
cell_size = 40
cell_number = 20

# Define the display surface
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

# Run a max speed clock
FramesPerSecond = pygame.time.Clock()

# Generate both the snake and the fruit
fruit = Fruit()
snake = Snake()

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
            snake.move_snake()
        # Get every event from the user that are key down related
        if event.type == pygame.KEYDOWN:
            # Go up if the key 'UP'/'W'/'Z' is pressed
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_z:
                snake.direction = Vector2(0, -1)
            # Go down if the key 'DOWN'/'S' is pressed
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake.direction = Vector2(0, 1)
            # Go right if the key 'RIGHT'/'D' is pressed
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake.direction = Vector2(1, 0)
            # Go left if the key 'LEFT'/'A'/'Q' is pressed
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_q:
                snake.direction = Vector2(-1, 0)

    # Apply some color on the display surface
    screen.fill((175, 215, 70))

    # Add the snake and fruit on the screen
    fruit.draw_fruit()
    snake.draw_snake()

    # Draw all our elements
    pygame.display.update()

    # Limit the speed of execution to 60 frames per second
    FramesPerSecond.tick(60)
