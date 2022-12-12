import sys
import pygame

# Init all pygame component
pygame.init()

# Define the display surface
screen = pygame.display.set_mode((400, 500))

# Run a max speed clock
FramesPerSecond = pygame.time.Clock()

# Create a surface to put on top of our display surface
test_surface = pygame.Surface((100, 200))

# Create a rectangle to put on top of our display surface it takes x, y, w, h
test_rectangle = pygame.Rect(100, 200, 100, 100)

while True:
    # Get all event that are happening in the game
    for event in pygame.event.get():
        # If the event is a click on the red x mark
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Apply some color on the display surface
    screen.fill((175, 215, 70))

    # Draw the rectangle on the screen by giving it the surface, the color and the rectangle
    pygame.draw.rect(screen, pygame.Color('red'), test_rectangle)

    # Apply our surface on top on the display surface at a position, relative to the top left corner, of 200 pixels and 250 pixels
    screen.blit(test_surface, (200, 250))

    # Draw all our elements
    pygame.display.update()

    # Limit the speed of execution to 60 frames per second
    FramesPerSecond.tick(60)

