# The class for the main character

import pygame

class Hero:
    def __init__(self, x, y, game):

        # Import the game
        self.game = game

        # Create a settings object
        self.settings = game.settings

        # Load the image
        self.image = pygame.image.load('Images/spaceship.png')

        # Resize image and get rect
        self.image = pygame.transform.scale(self.image, (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()

        # Set the x and y of the hero
        self.rect.x = x
        self.rect.y = y

        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def draw(self, screen):
        # Draw the hero at its current location
        screen.blit(self.image, self.rect)
    
    def update(self):
        # Update the hero's position based on the movement flag
        if self.moving_right and self.rect.right < self.settings.screen_width:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed