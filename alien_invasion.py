import pygame

import game_functions as gf
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

    # Main game loop
    while True:
        gf.check_events()
        gf.update_screen(settings, screen, ship)

# Start the game
run_game()
