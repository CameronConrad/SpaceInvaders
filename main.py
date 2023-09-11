# Space Invaders Game

import pygame
from settings import Settings

# Create a class for the game
class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Create a settings object
        self.settings = Settings()

        # Create a screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        