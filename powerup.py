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
        self.image = pygame.Surface((self.settings.powerup_radius * 2, self.settings.powerup_radius * 2))
        self.image.fill(self.settings.powerup_color)

        # Get the rect of the powerup
        self.rect = self.image.get_rect()

        # Set the center of the rect to the given center
        self.rect.centerx = centerx
        self.rect.centery = centery

        # Choose random powerup from bullet settings
        self.powerup = random.choice(list(self.settings.bullet_setting.keys()))
    
    def update(self):
        # Move the powerup down
        self.rect.y += self.settings.powerup_speed
    
    def draw(self, screen):
        # Draw the powerup
        pygame.draw.circle(screen, (255, 255, 255), (self.rect.centerx, self.rect.centery), 10)
