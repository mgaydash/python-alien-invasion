from pygame.sprite import Group

from bullet import Bullet

class Ship():
    """The ship controlled by the user"""

    def __init__(self, pygame, settings):
        self.pygame = pygame
        self.settings = settings
        self.screen = self.pygame.display.get_surface()
        self.speed = self.settings.ship_speed_factor
        self.moving_right = False
        self.moving_left = False

        # Make bullet group
        self.bullets = Group()

        # Load ship image and configure
        self.image = self.pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Configure the ship's starting postition
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

    def handle_event(self, event):
        if event.type == self.pygame.KEYDOWN:
            if event.key == self.pygame.K_SPACE:
                self.fire_bullet()

            if event.key == self.pygame.K_d:
                self.moving_right = True
            elif event.key == self.pygame.K_a:
                self.moving_left = True
        elif event.type == self.pygame.KEYUP:
            if event.key == self.pygame.K_d:
                self.moving_right = False
            elif event.key == self.pygame.K_a:
                self.moving_left = False

    
    def fire_bullet(self):
        """Fire a bullet"""
        
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(
                self.pygame,
                self.screen,
                self,
                self.settings.bullet_width,
                self.settings.bullet_height,
                self.settings.bullet_color,
                self.settings.bullet_speed_factor
            ))

    def update(self):
        """Update the ship's position and draw"""

        # Update location according to movement settings
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.speed
        self.rect.centerx = self.center

        # Update bullet locations
        self.bullets.update()

        # Remove bullets that leave the top of the screen (y = 0)
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Draw bullets
        for bullet in self.bullets.sprites():
            bullet.blit()

        # Draw
        self.screen.blit(self.image, self.rect)
