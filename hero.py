# The class for the main character

import pygame
from settings import Settings

class Hero:
    def __init__(self):
        # Create a settings object
        self.settings = Settings()

        # Load the image
        self.image = pygame.image.load('images/hero.bmp')

        # Resize image and get rect
        self.image = pygame.transform.scale(self.image, (self.settings.hero_width, self.settings.hero_height))
        self.rect = self.image.get_rect()

        # Start each new hero at the bottom center of the screen
        self.rect.midbottom = self.settings.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False