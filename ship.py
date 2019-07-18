import pygame

class Ship():
    """The ship controlled by the user"""

    def __init__(self, screen, speed):
        self.screen = screen
        self.speed = speed
        self.moving_right = False
        self.moving_left = False

        # Load ship image and configure
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Configure the ship's starting postition
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

    def blit(self):
        """Draw the ship at it's current location"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position according to movement settings"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.speed

        self.rect.centerx = self.center
