from pygame.sprite import Sprite

class Alien(Sprite):
    """Enemy alien spaceship"""

    speed = 1
    drop_speed = 10

    def __init__(self, pygame, x_location, y_location):
        super().__init__()
        self.pygame = pygame
        self.screen = self.pygame.display.get_surface()

        # This will be 1 or -1 to determine if the alien moves left or right
        self.direction = 1

        # Load alien image get related info
        self.image = self.pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Configure the alien's starting position
        self.rect.x = x_location
        self.rect.y = y_location

        # Store the x location as a float
        self.x = float(self.rect.x)

    def change_direction(self):
        """Switch between moving right and moving left"""

        self.direction *= -1

    def check_bottom(self):
        """Return True if the ship is at the bottom of the screen"""

        if self.rect.bottom >= self.screen_rect.bottom:
            return True

    def check_edges(self):
        """Return True if this Alien is at the edge of the screen"""

        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def drop(self):
        """Move down the screen by the given aount"""

        self.rect.y += Alien.drop_speed

    def get_height(self):
        """Return the height of the alien sprite"""

        return self.rect.height

    def get_width(self):
        """Return the width of the alien sprite"""

        return self.rect.width

    def update(self):
        """Update the alien's position and draw"""

        self.x += self.direction * Alien.speed
        self.rect.x = self.x

        # Draw
        self.screen.blit(self.image, self.rect)
