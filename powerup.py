# A class for a powerup

import pygame

class Powerup(pygame.sprite.Sprite):
    def __init__(self, centerx, centery, game):
        # Initialize the sprite
        pygame.sprite.Sprite.__init__(self)

        # Set the game
        self.game = game

        # Get settings
        self.settings = self.game.settings

        # Get the rect of the image
        self.rect = self.image.get_rect()

        # Set the center of the rect to the given center
        self.rect.centerx = centerx
        self.rect.centery = centery
    
    def update(self):
        # Move the powerup down
        self.rect.y += self.settings.powerup_speed
    
    def draw(self, screen):
        # Draw the powerup
        pygame.draw.circle(screen, (255, 255, 255), (self.rect.centerx, self.rect.centery), 10
