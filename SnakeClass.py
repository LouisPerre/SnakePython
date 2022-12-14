import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.tail = None
        self.head_img = None
        # Define the length of the positions snake in Vector so every block had a position
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        # Define all the assets for the snake
        self.head_up_image = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down_image = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right_image = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left_image = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up_image = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down_image = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right_image = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left_image = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical_image = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal_image = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr_image = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl_image = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br_image = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl_image = pygame.image.load('Graphics/body_bl.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def draw_snake(self, cell_size, screen):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            # Draw a rectangle with the position of every block in the snake and the width and height of the grid
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            # If the index is 0 the current block is the head
            if index == 0:
                screen.blit(self.head_img, block_rect)
            # If the index is the last element of the array so this is the tail
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            # Else this is the rest of our snake
            else:
                # We get the difference between the current block, the previous one and the next one,
                # If the x is equal between previous and next so they are horizontal, if the y is equal then they are verticale
                next_block = self.body[index + 1] - block
                previous_block = self.body[index - 1] - block
                if next_block.x == previous_block.x:
                    screen.blit(self.body_vertical_image, block_rect)
                elif next_block.y == previous_block.y:
                    screen.blit(self.body_horizontal_image, block_rect)
                else:
                    # Here we just check all the possible variations in x and y to select the correct image
                    if next_block.x == -1 and previous_block.y == -1 or next_block.y == -1 and previous_block.x == -1:
                        screen.blit(self.body_tl_image, block_rect)
                    elif next_block.x == -1 and previous_block.y == 1 or next_block.y == 1 and previous_block.x == -1:
                        screen.blit(self.body_bl_image, block_rect)
                    elif next_block.x == 1 and previous_block.y == -1 or next_block.y == -1 and previous_block.x == 1:
                        screen.blit(self.body_tr_image, block_rect)
                    elif next_block.x == 1 and previous_block.y == 1 or next_block.y == 1 and previous_block.x == 1:
                        screen.blit(self.body_br_image, block_rect)

    def move_snake(self):
        # If the snake eat an apple we copy the entire array if not we copy everything except the last
        if self.new_block:
            body_copy = self.body[:]
            self.new_block = False
        else:
            # If the snake don't eat an apple we just copy the entire array except the last element
            body_copy = self.body[:-1]
        # At every actualisation we insert a new head with the direction apply to it
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def update_head_graphics(self):
        # Check the Vector difference between the head and the next block to select the right image
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head_img = self.head_left_image
        elif head_relation == Vector2(-1, 0): self.head_img = self.head_right_image
        elif head_relation == Vector2(0, 1): self.head_img = self.head_up_image
        elif head_relation == Vector2(0, -1): self.head_img = self.head_down_image

    def update_tail_graphics(self):
        # Check the Vector difference between the tail and the previous block to select the right image
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left_image
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right_image
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up_image
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down_image

    def play_crunch_sound(self):
        # When the snake eat play the sound at a volume of 0.10
        self.crunch_sound.set_volume(0.10)
        self.crunch_sound.play()

    def reset(self):
        # Re-position the snake
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
