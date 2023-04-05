import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Class to handle the game"""

    def __init__(self):
        """Init the game"""
        pygame.init()
        self.clock = pygame.time.Clock()

        # Define properties
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption(self.settings.caption)

        # create ship object
        self.ship = Ship(self)
        # create bullet group
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            self._check_events()  # Check events
            self.ship.update()
            self._update_bullets()
            self._update_screen()  # Update content on screen
            self.clock.tick(self.settings.fps)  # 60fps

    def _check_events(self):
        # Handle inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Handle keypress events"""
        if event.key == pygame.K_RIGHT:
            # Move ship right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship right
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # Fire a bullet
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """ Handle keyup events"""
        if event.key == pygame.K_RIGHT:
            # Move ship right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Move ship right
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of the bullet and get rid of old bullet"""
        # Update bullet positions
        self.bullets.update()

        # Get rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        # Set screen options
        self.screen.fill(self.settings.bg_color)
        # Draw ship
        self.ship.blitme()
        # Draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Redraw the screen
        pygame.display.flip()


if __name__ == '__main__':
    # Create instance and run the game
    ai = AlienInvasion()
    ai.run_game()
