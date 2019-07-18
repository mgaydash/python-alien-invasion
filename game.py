from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet

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
        self.ship = Ship(self.screen, self.settings.ship_speed_factor)

        # Make bullet group
        self.bullets = Group()

        # Main game loop
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullets()
            self.update_screen()

    def check_events(self):
        """Respond to keypresses and mouse events"""

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.sys.exit()
            elif event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_d:
                    self.ship.moving_right = True
                elif event.key == self.pygame.K_a:
                    self.ship.moving_left = True
                elif event.key == self.pygame.K_SPACE:
                    self.fire_bullet()
            elif event.type == self.pygame.KEYUP:
                if event.key == self.pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == self.pygame.K_a:
                    self.ship.moving_left = False

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(
                self.pygame,
                self.screen,
                self.ship,
                self.settings.bullet_width,
                self.settings.bullet_height,
                self.settings.bullet_color,
                self.settings.bullet_speed_factor
            ))

    def update_bullets(self):
        """Update bullet position and delete offscreen bullets"""

        self.bullets.update()
        # Remove bullets that leave the top of the screen (y = 0)
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def update_screen(self):
        """Update images on the screen and flip to the new screen"""

        # Draw on screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blit()
        for bullet in self.bullets.sprites():
            bullet.blit()

        # This (oddly named) method draws the screen
        self.pygame.display.flip()
