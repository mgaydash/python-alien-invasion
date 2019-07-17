from settings import Settings
from ship import Ship

class Game():
    def __init__(self, pygame, sys):
        self.pygame = pygame
        self.sys = sys
        self.settings = Settings()

    def run(self):

        # Initialize the game and create our screen object
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((
            self.settings.screen_width, 
            self.settings.screen_height
        ))
        self.pygame.display.set_caption(self.settings.title)

        # Create ship
        self.ship = Ship(self.screen)

        # Main game loop
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        """Respond to keypresses and mouse events"""

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.sys.exit()

    def update_screen(self):
        """Update images on the screen and flip to the new screen"""

        # Draw on screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blit()

        # This (oddly named) method draws the screen
        self.pygame.display.flip()
