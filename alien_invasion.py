import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Class to handle the game"""

    def __init__(self):
        """Init the game"""
        pygame.init()

        # Define properties
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_heigt, self.settings.screen_width))
        pygame.display.set_caption(self.settings.caption)

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            # Handle inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Set screen options
            self.screen.fill(self.settings.bg_color)

            # Redraw the screen
            pygame.display.flip()


if __name__ == '__main__':
    # Create instance and run the game
    ai = AlienInvasion()
    ai.run_game()
