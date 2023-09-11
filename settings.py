# The settings for Space Invaders

class Settings:
    def __init__(self):
        # Set screen width and height
        self.screen_width = 800
        self.screen_height = 600

        # Set FPS
        self.fps = 60

        # Set the background color
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 3
        self.ship_width = 20
        self.ship_height = 20

        # Alien settings
        self.alien_rows = 3
        self.alien_columns = 10
        self.alien_width = 20
        self.alien_height = 20
        self.alien_speed = 3

        