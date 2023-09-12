# A class to manage bullets

import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, centerx, y, game):
        # Initialize the sprite
        super().__init__()

        # Import settings
        self.settings = game.settings

        # Create the bullet image
        self.image = pygame.Surface((self.settings.bullet_width, self.settings.bullet_height))
        self.image.fill(self.settings.bullet_color)

        # Get the rect of the bullet
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.y = y
        
    def update(self):
        # Move the bullet up the screen
        self.rect.y -= self.settings.bullet_speed
    
    def draw(self, screen):
        # If the bullet is off the screen, remove it
        if self.rect.bottom <= 0:
            return "miss"
        # Draw the bullet
        screen.blit(self.image, self.rect)
        return None