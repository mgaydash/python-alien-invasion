from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet fired from the ship"""

    speed = 1
    width = 3
    height = 15
    color = 60, 60, 60
    bullets_allowed = 3

    def __init__(self, pygame, screen, bullets, centerx, top):
        super().__init__()
        self.pygame = pygame
        self.screen = screen
        self.bullets = bullets

        # Create a bullet and set start position
        self.rect = pygame.Rect(0, 0, Bullet.width, Bullet.height)
        self.rect.centerx = centerx
        self.rect.top = top

        self.y = float(self.rect.y)

    def update(self):
        """Update the bullet's position and draw"""

        self.y -= Bullet.speed
        self.rect.y = self.y

        # Remove bullets that leave the top of the screen (y = 0)
        if self.rect.bottom <= 0:
            self.bullets.remove(self)

        self.pygame.draw.rect(self.screen, self.color, self.rect)
