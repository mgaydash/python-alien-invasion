from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet fired from the ship"""

    def __init__(self, pygame, screen, ship, width, height, color, speed):
        super().__init__()
        self.pygame = pygame
        self.screen = screen
        self.color = color
        self.speed = speed

        # Create a bullet and set start position
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

    def blit(self):
        """Draw the bullet on the screen at it's current position"""
        self.pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """Update the bullet's position according to movement settings"""

        self.y -= self.speed
        self.rect.y = self.y
