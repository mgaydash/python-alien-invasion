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
        alien = Alien(self.pygame, 0, 0)

        # Want to allow padding of 2 * the sprite width
        available_space_x = Game.screen_width - 2 * alien.get_width()

        # How many aliens can we fit? Allow padding between of 1 alien width
        num_aliens_x = int(available_space_x / (2 * alien.get_width()))

        # How much height do we have to work with?
        # Screen height - 2 aliens of space at the bottom and one at the top - ship height
        available_space_y = Game.screen_height - 3 * alien.get_height() - self.ship.get_height()

        # Allow padding between rows of 1 alien height
        num_rows = int(available_space_y / (2 * alien.get_height()))

        # Create rows of aliens
        for row_num in range(num_rows):
            for alien_num in range(num_aliens_x):
                alien_x = alien.get_width() + 2 * alien.get_width() * alien_num
                alien_y = alien.get_height() + 2 * alien.get_height() * row_num
                self.aliens.add(Alien(self.pygame, alien_x, alien_y))
