import sys
import pygame

from settings import Settings
from ship import Ship

settings = Settings()

def run_game():
    # Initialize the game and create our screen object
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    # Create ship
    ship = Ship(screen)

    # This is the main game loop
    while True:

        # This loop is for responding to user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Draw on screen
        screen.fill(settings.bg_color)
        ship.blit()

        # This (oddly named) method draws the screen
        pygame.display.flip()

# Start the game
run_game()