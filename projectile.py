# A class to manage projectiles fired by the aliens

import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, centerx, centery, game):
        # Initialize the sprite
        pygame.sprite.Sprite.__init__(self)

        # Set the game
        self.game = game

        # Get settings
        self.settings = self.game.settings

        # Create the image of the projectile
        self.image = pygame.Surface((self.settings.projectile_width, self.settings.projectile_height))
        self.image.fill(self.settings.projectile_color)

        # Get the rect of the projectile
        self.rect = self.image.get_rect()

        # Set the center of the rect to the given center
        self.rect.centerx = centerx
        self.rect.centery = centery

        # Set the speed
        self.speed = self.settings.projectile_speed
    
    def update(self):
        # Move the projectile down
        self.rect.y += self.speed

        # Check if the projectile is off the screen
        if self.rect.top > self.game.screen_rect.bottom:
            self.kill()