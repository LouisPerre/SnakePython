import pygame, random
from pygame.math import Vector2


class Fruit:
    def __init__(self, grid_number):
        self.x = 0
        self.y = 0
        self.position = Vector2(0, 0)
        self.randomize_position(grid_number)

    def draw_fruit(self, cell_size, screen, apple):
        # Draw the fruit on the screen
        fruit_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize_position(self, grid_number):
        # Get a random position for the fruit
        self.x = random.randint(0, grid_number - 1)
        self.y = random.randint(0, grid_number - 1)
        self.position = Vector2(self.x, self.y)
        