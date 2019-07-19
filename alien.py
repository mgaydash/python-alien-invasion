class Alien():
    """Enemy alien spaceship"""

    def __init__(self, pygame):
        self.pygame = pygame
        self.screen = self.pygame.display.get_surface()

        # Load alien image get related info
        self.image = self.pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Configure the alien's starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the x location as a float
        self.x = float(self.rect.x)

    def update(self):
        """Update the alien's position and draw"""

        # Draw
        self.screen.blit(self.image, self.rect)
