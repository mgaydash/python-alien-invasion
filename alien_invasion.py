import sys
import pygame


def run_game():
    # Initialize the game and create our screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    # This is the main game loop
    while True:

        # This loop is for responding to user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        # This (oddly named) method draws the screen
        pygame.display.flip()

# Start the game
run_game()