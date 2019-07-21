from pygame.sprite import Sprite

class Alien(Sprite):
    """Enemy alien spaceship"""

    def __init__(self, pygame, x_location):
        super().__init__()
        self.pygame = pygame
        self.screen = self.pygame.display.get_surface()

        # Load alien image get related info
        self.image = self.pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Configure the alien's starting position
        self.rect.x = x_location
        self.rect.y = self.rect.height

        # Store the x location as a float
        self.x = float(self.rect.x)

    def get_width(self):
        """Return the width of the alien sprite"""

        return self.rect.width

    def update(self):
        """Update the alien's position and draw"""

        # Draw
        self.screen.blit(self.image, self.rect)
