from pygame.sprite import Group

from bullet import Bullet

class Ship():
    """The ship controlled by the user"""

    bullets_allowed = 3
    speed = 1.5

    def __init__(self, pygame):
        self.pygame = pygame
        self.screen = self.pygame.display.get_surface()
        self.moving_right = False
        self.moving_left = False

        # Bullet group to track fired bullets
        self.bullets = Group()

        # Load ship image and get related info
        self.image = self.pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Configure the ship's starting postition
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

    def handle_event(self, event):
        """Respond to events such as user input"""

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
        
        if len(self.bullets) < Ship.bullets_allowed:
            self.bullets.add(Bullet(
                self.pygame,
                self.screen,
                self.bullets,
                self.rect.centerx,
                self.rect.top
            ))

    def get_height(self):
        return self.rect.height

    def update(self):
        """Update the ship's position and draw"""

        # Update location according to movement settings
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += Ship.speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= Ship.speed
        self.rect.centerx = self.center

        # Update and draw bullets
        self.bullets.update()

        # Draw
        self.screen.blit(self.image, self.rect)
