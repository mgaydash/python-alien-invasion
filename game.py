from ship import Ship
from bullet import Bullet
from alien import Alien

class Game():
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
        self.alien = Alien(self.pygame)

        # Main game loop
        while True:
            self.check_events()

            # Draw on screen
            self.screen.fill(Game.bg_color)

            self.ship.update()
            self.alien.update()

            # This (oddly named) method draws the screen
            self.pygame.display.flip()

    def check_events(self):
        """Respond to keypresses and mouse events"""

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.sys.exit()
            else:
                self.ship.handle_event(event)
