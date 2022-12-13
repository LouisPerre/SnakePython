import sys
import pygame
import random
from pygame.math import Vector2


# Create a Fruit class which generate a random position with Vector to a better manipulation of its coord, also add a method to create and draw the fruit on the map
class Fruit:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = Vector2(0, 0)
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)

        # Apply the image of apple inside the rectangle
        screen.blit(apple, fruit_rect)

        # Draw a rectangle on the screen with a color inside the rectangle
        #pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)


class Snake:
    def __init__(self):
        # Represent the length and position of our snake
        self.tail = None
        self.head = None
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        # Represent the moving direction for the snake
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        #for block in self.body:
        #    # Create a rectangle from the pos and draw the rectangle
        #    block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
        #    pygame.draw.rect(screen, (183, 111, 122), block_rect)

        for index, block in enumerate(self.body):
            # Create a rectangle for the positioning, What direction is the face heading
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                next_block = self.body[index + 1] - block
                previous_block = self.body[index - 1] - block
                if next_block.x == previous_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif next_block.y == previous_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if next_block.x == -1 and previous_block.y == -1 or next_block.y == -1 and previous_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif next_block.x == -1 and previous_block.y == 1 or next_block.y == 1 and previous_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif next_block.x == 1 and previous_block.y == -1 or next_block.y == -1 and previous_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif next_block.x == 1 and previous_block.y == 1 or next_block.y == 1 and previous_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            self.new_block = False
        else:
            # Copy the body properties except the last one
            body_copy = self.body[:-1]
        # Insert a new item right at the start for the new position of the head
        body_copy.insert(0, body_copy[0] + self.direction)
        # Assign the new position to the self property
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down

    def play_crunch_sound(self):
        self.crunch_sound.set_volume(0.09)
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            # Reposition the fruit and add another block to the snake
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.position:
                self.fruit.randomize()

    def check_fail(self):
        # Check if snake is outside of the screen and if snake hits itself
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for column in range(cell_number):
                    if column % 2 == 0:
                        grass_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for column in range(cell_number):
                    if column % 2 != 0:
                        grass_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))

        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)


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
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

main_game = Main()

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
