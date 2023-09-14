# Space Invaders Game

import pygame
import sys
import random
from settings import Settings
from hero import Hero
from alien import Alien
from bullet import Bullet
from projectile import Projectile
from powerup import Powerup
from scoreboard import Scoreboard

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
        self.spawn_hero()

        # Create a sprite group for the aliens
        self.aliens = pygame.sprite.Group()

        # Create a sprite group for the bullets
        self.bullets = pygame.sprite.Group()

        # Create a sprite group for the powerups
        self.powerups = pygame.sprite.Group()

        # Create a sprite group for the projectiles
        self.projectiles = pygame.sprite.Group()

        # Create level variable
        self.level = 1

        # Initialize the scoreboard
        self.scoreboard = Scoreboard(self.screen_rect.centerx, self.screen_rect.bottom - 50, self)

        # Set run to false
        self.run = False
    
    def spawn_aliens(self):
        # Spawn the aliens
        for i in range(self.settings.alien_rows):
            for j in range(self.settings.alien_columns):
                alien = Alien(j * self.settings.alien_width + 5, i * self.settings.alien_height, self)
                self.aliens.add(alien)
    
    def spawn_hero(self):
        # Spawn the hero
        self.hero = Hero(self.screen_rect.centerx, self.screen_rect.bottom - 150, self)
    
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
            self.shoot_bullet()

    def shoot_bullet(self):
            # Create a bullet and add it to the bullets group
            bullet = Bullet(self.hero.rect.centerx, self.hero.rect.top, self)
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
        # If bullet setting is invincible, do not destroy the bullet
        if self.settings.bullet_type == 'invincible':
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        else:
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if len(collisions) > 0:
            self.scoreboard.increase_stat(hits=len(collisions))
            if len(self.aliens) == 0:
                self.reset_game(level_up=True)
    
    def check_hero_alien_collisions(self):
        # Check for collisions between the hero and aliens
        collisions = pygame.sprite.spritecollide(self.hero, self.aliens, False)
        if len(collisions) > 0:
            self.reset_game()
    
    def check_hero_powerup_collisions(self):
        collisions = pygame.sprite.spritecollide(self.hero, self.powerups, True)
        if len(collisions) > 0:
            print(collisions[0].powerup)
            self.settings.change_bullet_setting(collisions[0].powerup)
    
    def check_hero_projectile_collisions(self):
        collisions = pygame.sprite.spritecollide(self.hero, self.projectiles, True)
        if len(collisions) > 0:
            self.reset_game()
    
    def reset_game(self, level_up = False):
        # Reset the game
        self.spawn_hero()
        self.aliens.empty()
        self.bullets.empty()
        self.spawn_aliens()
        if level_up:
            self.level_up()
            self.scoreboard.increase_stat(wins=1)
        else:
            self.settings.change_bullet_setting('normal')
            self.scoreboard.increase_stat(losses=1)

    def level_up(self):
        # Increase the level
        self.level += 1
        # Increase alien speed
        for alien in self.aliens:
            self.settings.alien_speed += self.settings.alien_speed_increase
    
    def run_game(self):
        self.spawn_aliens()
        self.run = True
        loop = 0
        while self.run:
            # Randomly spawn a powerup once every set number of frames
            if loop % self.settings.powerup_odds == 0:
                powerup = Powerup(random.randint(0, self.settings.screen_width), 0, self)
                self.powerups.add(powerup)
             
            # Randomly spawn a projectile at the position of a random alien once every set number of frames
            if loop % self.settings.projectile_odds == 0 and loop != 0:
                alien = random.choice(self.aliens.sprites())
                projectile = Projectile(alien.rect.centerx, alien.rect.centery, self)
                self.projectiles.add(projectile)
                
            # Set the FPS
            self.clock.tick(self.settings.fps)

            # Check events
            self.check_events()

            # Update sprites
            self.check_alien_position()
            self.hero.update()
            self.aliens.update()
            self.bullets.update()
            self.projectiles.update()
            self.powerups.update()
            self.scoreboard.update()

            # Check for collisions
            self.check_bullet_alien_collisions()
            self.check_hero_alien_collisions()
            self.check_hero_powerup_collisions()
            self.check_hero_projectile_collisions()

            # Redraw the screen
            self.screen.fill(self.settings.bg_color)

            # Draw sprites on the screen
            self.hero.draw(self.screen)
            self.aliens.draw(self.screen)
            for bullet in self.bullets.sprites():
                if bullet.draw(self.screen) == "miss":
                    self.bullets.remove(bullet)
                    self.scoreboard.increase_stat(misses=1)
            self.projectiles.draw(self.screen)
            self.powerups.draw(self.screen)
            self.scoreboard.draw(self.screen)

            # Update the screen
            pygame.display.update()

            # Increase loop count
            loop += 1
            
            
# Run the game
if __name__ == '__main__':
    game = Game()
    game.run_game()