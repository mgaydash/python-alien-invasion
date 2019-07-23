from alien_fleet import AlienFleet
from ship import Ship
from bullet import Bullet
from alien import Alien

class Game():
    """Top-level game class containing the main event loop"""

    screen_width = 1200
    screen_height = 800
    bg_color = (230, 230, 230)
    title = "Alien Invasion"

    def __init__(self, pygame, sys, time):
        self.pygame = pygame
        self.sys = sys
        self.time = time
        self.lives = 3

    def check_events(self):
        """Respond to keypresses and mouse events"""

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.sys.exit()
            else:
                self.ship.handle_event(event)

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
            self.fleet.handle_collisions(self.ship.get_bullets())
            self.fleet.update()

            # If the fleet has been destroyed, create a new fleet
            if 0 == self.fleet.get_remaining():
                self.fleet = AlienFleet(self.pygame, available_space_x, available_space_y)

            # Handle aliens colliding with the ship
            if self.fleet.check_ship_collision(self.ship):
                self.lives -= 1

                # Reset the ship and fleet, redraw
                self.fleet = AlienFleet(self.pygame, available_space_x, available_space_y)
                self.ship = Ship(self.pygame)
                self.pygame.display.flip()

                # Pause the game for .5 sec so the restart is noticable
                self.time.sleep(0.5)

            # Draw the "hud"
            self.update_hud()

            # This (oddly named) method draws the screen
            self.pygame.display.flip()

    def update_hud(self):
        font = self.pygame.font.SysFont("Courier", 24)
        lives_text = font.render("Lives Remaining: " + str(self.lives), True, (4, 4, 4))
        self.screen.blit(lives_text, (10, 10))
