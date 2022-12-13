import pygame, random
from pygame.math import Vector2


class Fruit:
    def __init__(self, cell_number):
        self.x = 0
        self.y = 0
        self.position = Vector2(0, 0)
        self.randomize(cell_number)

    def draw_fruit(self, cell_size, screen, apple):
        fruit_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self, cell_number):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
        