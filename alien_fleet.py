from pygame.sprite import Group

from alien import Alien

class AlienFleet():
    """Manages the alien ship fleet"""

    def __init__(self, pygame, space_x, space_y):
        self.pygame = pygame
        self.aliens = Group()

        # Create an example alien to use for measurment
        alien = Alien(self.pygame, 0, 0)

        # How many aliens can we fit? Allow padding between of 1 alien width
        num_aliens_x = int(space_x / (2 * alien.get_width()))

        # Allow padding between rows of 1 alien height
        num_rows = int(space_y / (2 * alien.get_height()))

        # Create rows of aliens
        for row_num in range(num_rows):
            for alien_num in range(num_aliens_x):
                alien_x = alien.get_width() + 2 * alien.get_width() * alien_num
                alien_y = alien.get_height() + 2 * alien.get_height() * row_num
                self.aliens.add(Alien(self.pygame, alien_x, alien_y))

    def change_direction(self):
        """Change the direction of all aliens in the fleet"""

        for alien in self.aliens.sprites():
            alien.change_direction()
            alien.drop()

    def update(self):
        """Update the aliens' position and draw"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_direction()
                break

        self.aliens.update()
        