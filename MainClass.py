import sys, pygame, time, csv, os
from FruitClass import Fruit
from SnakeClass import Snake
from ScoreClass import Score


class Main:
    def __init__(self, grid_number, grid_size, screen):
        self.grid_number = grid_number
        self.grid_size = grid_size
        self.snake = Snake()
        self.fruit = Fruit(grid_number)
        self.apple = pygame.image.load('Graphics/apple.png').convert_alpha()
        self.game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
        self.screen = screen
        self.dead = False
        self.start = time.time()
        self.score_class = Score()

    def update(self):
        # Update the position of snake, check for collision with an apple and fail
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        # If the snake is not dead, draw the grass, new position of fruit and snake and the score
        if not self.dead:
            self.draw_grass()
            self.fruit.draw_fruit(self.grid_size, self.screen, self.apple)
            self.snake.draw_snake(self.grid_size, self.screen)
            self.draw_score()
        if self.dead:
            self.dead = self.score_class.draw_end_screen(self.snake, self.start, self.screen, self.apple, self.grid_size,
                                                 self.grid_number, self.game_font, self.dead)

    def check_collision(self):
        # If the position of the fruit and the head of the snake ar on the same point, he ate it
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize_position(self.grid_number)
            self.snake.add_block()
            self.snake.play_crunch_sound()
        # If the fruit spawn on the body of the snake we re-spawn the fruit
        for block in self.snake.body[1:]:
            if block == self.fruit.position:
                self.fruit.randomize_position(self.grid_number)

    def check_fail(self):
        # If the snake is outside the screen we check the length of the snake body
        if not 0 <= self.snake.body[0].x < self.grid_number or not 0 <= self.snake.body[0].y < self.grid_number:
            # If the length is above 3 then we draw the score screen else we just re-render the game
            if len(self.snake.body) > 3:
                self.dead = True
                self.dead = self.score_class.draw_end_screen(self.snake, self.start, self.screen, self.apple, self.grid_size,
                                                 self.grid_number, self.game_font, self.dead)
            else:
                self.game_over()
        # If the snake hit himself and its length is above 3 we draw the dead screen
        for block in self.snake.body[1:]:
            if block == self.snake.body[0] and len(self.snake.body) > 3:
                self.dead = True
                self.dead = self.score_class.draw_end_screen(self.snake, self.start, self.screen, self.apple, self.grid_size, self.grid_number, self.game_font, self.dead)
            elif block == self.snake.body[0]:
                self.game_over()

    # Reset the game, position and length of the snake
    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        # Draw the grass with a specific color, the odd block are slightly darker than the even one
        grass_color = (167, 209, 61)
        for row in range(self.grid_number):
            if row % 2 == 0:
                for column in range(self.grid_number):
                    if column % 2 == 0:
                        grass_rect = pygame.Rect(column * self.grid_size, row * self.grid_size, self.grid_size, self.grid_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
            else:
                for column in range(self.grid_number):
                    if column % 2 != 0:
                        grass_rect = pygame.Rect(column * self.grid_size, row * self.grid_size, self.grid_size, self.grid_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)

    def draw_score(self):
        # Draw the score in the bottom right corner, get the right text
        score_text = str(len(self.snake.body) - 3)
        # Render the text and prepare it to be rendered
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        # Get the right point to position it precisely
        score_x = int(self.grid_size * self.grid_number - 60)
        score_y = int(self.grid_size * self.grid_number - 40)
        # Generate rect for two elements of the score board
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = self.apple.get_rect(midright=(score_rect.left, score_rect.centery))

        # Apply the new elements on the screen
        self.screen.blit(score_surface, score_rect)
        self.screen.blit(self.apple, apple_rect)
