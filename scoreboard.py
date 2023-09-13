# A class for the scoreboard

import pygame

class Scoreboard:
    def __init__(self, centerx, centery, game):
        # Import game
        self.game = game

        # Load settings
        self.settings = game.settings

        # Initialize stats
        self.hits = 0
        self.misses = 0
        self.accuracy = 0
        self.wins = 0
        self.losses = 0
        self.win_rate = 0
        
        # Load Aoki font
        self.font = pygame.font.Font('Aoki Regular.otf', 30)

        # Create the text for the scoreboard
        self.create_text()

        # Create rounded rectangle for the scoreboard
        self.rect = pygame.Rect(0, 0, self.settings.scoreboard_width, self.settings.scoreboard_height)
        self.rect.center = (centerx, centery)

        # Create the image for the scoreboard
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill(self.settings.scoreboard_bg_color)
    
    def create_text(self):
        # Create the text for the scoreboard
        self.accuracy_text = self.font.render(f'A: {self.accuracy}', True, self.settings.scoreboard_text_color)
        self.win_rate_text = self.font.render(f'Win %: {self.win_rate}', True, self.settings.scoreboard_text_color)
        self.level_text = self.font.render(f'Level: {self.game.level}', True, self.settings.scoreboard_text_color)

    def increase_stat(self, hits=0, misses=0, wins=0, losses=0):
        # Increase the stat
        self.hits += hits
        self.misses += misses
        self.wins += wins
        self.losses += losses

        # Update the scoreboard
        self.update()

    def update(self):
        # Update the stats
        if self.hits + self.misses > 0:
            self.accuracy = round(self.hits / (self.hits + self.misses), 3)
        if self.wins + self.losses > 0:
            self.win_rate = round(self.wins / (self.wins + self.losses), 3)
    
    def draw(self, screen):
        # Update the scoreboard
        self.create_text()
        self.image.fill(self.settings.scoreboard_bg_color)

        # Draw the scoreboard
        pygame.draw.rect(screen, self.settings.scoreboard_bg_color, self.rect, border_radius=10)

        # Draw the text all in one line so that it is centered
        screen.blit(self.accuracy_text, (self.rect.left + 10, self.rect.top + 10))
        screen.blit(self.win_rate_text, (self.rect.centerx - (self.win_rate_text.get_width() / 2), self.rect.top + 10))
        screen.blit(self.level_text, (self.rect.right - 10 - self.level_text.get_width(), self.rect.top + 10))