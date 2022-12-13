import pygame


class Game:
    def __init__(self, cell_number, cell_size):
        # Create all the element that we need to launch a game
        self.launch_game()
        # Define the width and height of the screen
        self.screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
        # Launch a clock to define the fps of the game
        self.frames_per_second = pygame.time.Clock()

    def launch_game(self):
        # Preload all the sound to prevent delays
        pygame.mixer.pre_init(44100, -16, 2, 512)
        # Launch all the pygame elements
        pygame.init()
        # Set the title and logo of the screen
        pygame.display.set_caption('Snake')
        logo = pygame.image.load('./Graphics/logo/Snake01.png')
        pygame.display.set_icon(logo)

    def screen_color(self):
        self.screen.fill((175, 215, 70))

    def screen_update(self):
        # Update the screen to apply every modification
        pygame.display.update()
        # Set the cap frame rate to 60
        self.frames_per_second.tick(60)
