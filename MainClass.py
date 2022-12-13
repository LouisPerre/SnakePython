from FruitClass import Fruit
from SnakeClass import Snake
import pygame


class Main:
    def __init__(self, cell_number, cell_size, screen):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.snake = Snake()
        self.fruit = Fruit(cell_number)
        self.apple = pygame.image.load('Graphics/apple.png').convert_alpha()
        self.game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
        self.screen = screen
        self.dead = False

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        if not self.dead:
            self.draw_grass()
            self.fruit.draw_fruit(self.cell_size, self.screen, self.apple)
            self.snake.draw_snake(self.cell_size, self.screen)
            self.draw_score()
        if self.dead:
            self.draw_end_screen()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize(self.cell_number)
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.position:
                self.fruit.randomize(self.cell_number)

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0] and len(self.snake.body) > 3:
                self.dead = True
                self.draw_end_screen()
            elif block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(self.cell_number):
            if row % 2 == 0:
                for column in range(self.cell_number):
                    if column % 2 == 0:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
            else:
                for column in range(self.cell_number):
                    if column % 2 != 0:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(self.cell_size * self.cell_number - 60)
        score_y = int(self.cell_size * self.cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = self.apple.get_rect(midright=(score_rect.left, score_rect.centery))

        self.screen.blit(score_surface, score_rect)
        self.screen.blit(self.apple, apple_rect)

    def draw_end_screen(self):
        self.screen.fill((175, 215, 70))
        score_text = 'Your highest score is' + str(len(self.snake.body) - 3)
        print('Your highest score is' + str(len(self.snake.body) - 3))
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int((self.cell_size * self.cell_number) / 2)
        score_y = int((self.cell_size * self.cell_number) / 2)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        self.screen.blit(score_surface, score_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    self.snake.reset()
                    self.dead = False

