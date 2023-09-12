# Space Invaders Game

import pygame
import sys
from settings import Settings
from hero import Hero
from alien import Alien
from bullet import Bullet

# Create a class for the game
class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Create a settings object
        self.settings = Settings()

        # Create a clock
        self.clock = pygame.time.Clock()

        # Create a screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        self.screen_rect = self.screen.get_rect()

        # Set caption
        pygame.display.set_caption('Space Invaders')

        # Create the hero object
        self.hero = Hero(self.screen_rect.centerx, self.screen_rect.bottom - 50)

        # Create a sprite group for the aliens
        self.aliens = pygame.sprite.Group()

        # Create a sprite group for the bullets
        self.bullets = pygame.sprite.Group()

        # Create level variable
        self.level = 1

        # Set run to false
        self.run = False
    
    def spawn_aliens(self):
        # Spawn the aliens
        for i in range(self.settings.alien_rows):
            for j in range(self.settings.alien_columns):
                alien = Alien(j * self.settings.alien_width + 5, i * self.settings.alien_height)
                self.aliens.add(alien)
    
    def check_alien_position(self):
        # Check if either side of the alien block reaches the edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                move = 0
                if alien.rect.left < 0:
                    move = -alien.rect.left
                elif alien.rect.right > self.settings.screen_width:
                    move = self.settings.screen_width - alien.rect.right
                self.change_alien_direction(move)
                break

    def change_alien_direction(self, move: int):
        for alien in self.aliens.sprites():
            alien.change_direction(move)
    
    def check_keydown_events(self, event):
        # Respond to keypresses
        if event.key == pygame.K_RIGHT:
            self.hero.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.hero.moving_left = True
        elif event.key == pygame.K_SPACE:
            # Create a bullet and add it to the bullets group
            bullet = Bullet(self.hero.rect.centerx, self.hero.rect.top)
            self.bullets.add(bullet)
        
    def check_keyup_events(self, event):
        # Respond to key releases
        if event.key == pygame.K_RIGHT:
            self.hero.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.hero.moving_left = False
    
    def check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
    
    def check_bullet_alien_collisions(self):
        # Check for collisions between bullets and aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if len(self.aliens) == 0:
            self.reset_game(True)
    
    def check_hero_alien_collisions(self):
        # Check for collisions between the hero and aliens
        collisions = pygame.sprite.spritecollide(self.hero, self.aliens, False)
        if len(collisions) > 0:
            self.reset_game()
    
    def reset_game(self, level_up = False):
        # Reset the game
        self.hero = Hero(self.screen_rect.centerx, self.screen_rect.bottom - 50)
        self.aliens.empty()
        self.bullets.empty()
        self.spawn_aliens()
        if level_up:
            self.level_up()

    def level_up(self):
        # Increase the level
        self.level += 1
        # Increase alien speed
        for alien in self.aliens:
            alien.settings.alien_speed += self.settings.alien_speed_increase
    
    def run_game(self):
        self.spawn_aliens()
        self.run = True
        while self.run:
            # Set the FPS
            self.clock.tick(self.settings.fps)

            # Check events
            self.check_events()

            # Update sprites
            self.check_alien_position()
            self.hero.update()
            self.aliens.update()
            self.bullets.update()

            # Check for collisions
            self.check_bullet_alien_collisions()
            self.check_hero_alien_collisions()

            # Redraw the screen
            self.screen.fill(self.settings.bg_color)

            # Draw sprites on the screen
            self.hero.draw(self.screen)
            self.aliens.draw(self.screen)
            self.bullets.draw(self.screen)

            # Update the screen
            pygame.display.update()
            
            
# Run the game
if __name__ == '__main__':
    game = Game()
    game.run_game()