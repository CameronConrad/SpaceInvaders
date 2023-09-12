# A class for the alien

import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        # Initialize the alien and set its starting position
        super().__init__()

        # Import the game
        self.game = game

        # Load the image
        self.image = pygame.image.load('Images/alien.png')

        # Load settings
        self.settings = game.settings

        # Resize image and get rect
        self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height))
        self.rect = self.image.get_rect()

        # Start each new alien at the top left of the screen
        self.rect.x = x
        self.rect.y = y

        # Movement flag
        self.moving_right = True
        self.moving_left = False
    
    def draw(self, screen):
        # Draw the alien at its current location
        screen.blit(self.image, self.rect)
    
    def change_direction(self, move: int):
        # Change the direction of the alien
        self.moving_right = not self.moving_right
        self.moving_left = not self.moving_left
        self.rect.x += move
        self.rect.y += self.settings.alien_height

    def check_edges(self):
        # Check if the alien has reached the edge
        if self.rect.right >= self.settings.screen_width or self.rect.left <= 0:
            return True
        else:
            return False
    
    def update(self):
        # Update the alien's position based on the movement flag
        if self.moving_right:
            self.rect.x += self.settings.alien_speed
        if self.moving_left:
            self.rect.x -= self.settings.alien_speed
        