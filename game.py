from alien_fleet import AlienFleet
from ship import Ship
from bullet import Bullet
from alien import Alien

class Game():
    """Top-level game class conteinint the main event loop"""

    screen_width = 1200
    screen_height = 800
    bg_color = (230, 230, 230)
    title = "Alien Invasion"

    def __init__(self, pygame, sys):
        self.pygame = pygame
        self.sys = sys

    def run(self):
        # Initialize the game and create our screen object
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((
            Game.screen_width, 
            Game.screen_height
        ))
        self.pygame.display.set_caption(Game.title)

        self.ship = Ship(self.pygame)

        # How much space do we want to use to draw alien ships?
        # Create an example alien to use for measurment
        alien = Alien(self.pygame, 0, 0)
        available_space_x = Game.screen_width - 2 * alien.get_width()
        available_space_y = Game.screen_height - 3 * alien.get_height() - self.ship.get_height()
        self.fleet = AlienFleet(self.pygame, available_space_x, available_space_y)

        # Main game loop
        while True:
            self.check_events()

            # Draw on screen
            self.screen.fill(Game.bg_color)

            self.ship.update()
            self.fleet.update()

            # This (oddly named) method draws the screen
            self.pygame.display.flip()

    def check_events(self):
        """Respond to keypresses and mouse events"""

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.sys.exit()
            else:
                self.ship.handle_event(event)
