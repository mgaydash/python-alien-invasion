from pygame.sprite import Group

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
        self.aliens = Group()
        self.create_fleet()

        # Main game loop
        while True:
            self.check_events()

            # Draw on screen
            self.screen.fill(Game.bg_color)

            self.ship.update()
            self.aliens.update()

            # This (oddly named) method draws the screen
            self.pygame.display.flip()

    def check_events(self):
        """Respond to keypresses and mouse events"""

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.sys.exit()
            else:
                self.ship.handle_event(event)

    def create_fleet(self):
        """Create a full fleet of aliens"""

        # Create an example alien to use for measurment
        alien = Alien(self.pygame, 0)
        alien_width = alien.get_width()

        # Want to allow padding of 2 * the sprite width
        available_space_x = Game.screen_width - 2 * alien_width

        # How many aliens can we fit? Allow padding between of 1 alien width
        num_aliens_x = int(available_space_x / (2 * alien_width))

        # Create rows of aliens
        for alien_num in range(num_aliens_x):
            alien_x = alien_width + 2 * alien_width * alien_num
            self.aliens.add(Alien(self.pygame, alien_x))
