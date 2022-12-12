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

# Draw a rectangle around my existing surface allowing me to move its origin point
test_rectangle = test_surface.get_rect(center=(200, 250))

while True:
    # Get all event that are happening in the game
    for event in pygame.event.get():
        # If the event is a click on the red x mark
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Apply some color on the display surface
    screen.fill((175, 215, 70))

    # Apply our surface on top on the display surface at a position directed by the rectangle created above
    screen.blit(test_surface, test_rectangle)

    # Draw all our elements
    pygame.display.update()

    # Limit the speed of execution to 60 frames per second
    FramesPerSecond.tick(60)

