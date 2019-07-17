import pygame

class Ship():
    """The ship controlled by the user"""

    def __init__(self, screen):
        self.screen = screen

        # Load ship image and configure
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Configure the ship's starting postition
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blit(self):
        """Draw the ship at it's current location"""

        self.screen.blit(self.image, self.rect)
