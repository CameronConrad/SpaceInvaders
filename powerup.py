# A class for a powerup

import pygame
import random

class Powerup(pygame.sprite.Sprite):
    def __init__(self, centerx, centery, game):
        # Initialize the sprite
        pygame.sprite.Sprite.__init__(self)

        # Set the game
        self.game = game

        # Get settings
        self.settings = self.game.settings

        # Create the image of the powerup
        self.image = pygame.Surface((self.settings.powerup_width, self.settings.powerup_height))
        self.image.fill(self.settings.powerup_color)

        # Get the rect of the powerup
        self.rect = self.image.get_rect()

        # Set the center of the rect to the given center
        self.rect.centerx = centerx
        self.rect.centery = centery

        # Choose random powerup from bullet settings based on the odds of the bullet setting
        weights = [self.settings.bullet_setting[key][3] for key in self.settings.bullet_setting]
        self.powerup = random.choices(list(self.settings.bullet_setting.keys()), weights=weights)[0]

    def update(self):
        # Move the powerup down
        self.rect.y += self.settings.powerup_speed
