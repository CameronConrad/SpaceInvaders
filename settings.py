# The settings for Space Invaders

class Settings:
    def __init__(self):
        # Set screen width and height
        self.screen_width = 1000
        self.screen_height = 700

        # Set FPS
        self.fps = 60

        # Set the background color to black
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 4
        self.ship_width = 30
        self.ship_height = 30

        # Alien settings
        self.alien_rows = 5
        self.alien_columns = 10
        self.alien_width = 30
        self.alien_height = 30
        self.alien_speed = 1

        # Bullet settings
        self.bullet_speed = 12
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255, 0, 0)

        self.bullet_setting = {
            # Each setting has a list of bullet attributes corresponding to speed, width, and height.
            'normal': [12, 5, 10], # 12 speed, 5 width, 10 height
            'speed': [20, 5, 10], # 20 speed, 5 width, 10 height
            'size': [12, 30, 20], # 12 speed, 30 width, 20 height
            'invincible': [12, 5, 10] # 12 speed, 5 width, 10 height
        }

        # Powerup settings
        self.powerup_width = 20
        self.powerup_height = 20
        self.powerup_color = (255, 255, 255)
        self.powerup_speed = 5

        # Level up settings
        self.alien_speed_increase = 0.05

        # Score settings
        self.scoreboard_bg_color = (0, 0, 255)
        self.scoreboard_text_color = (255, 255, 255)
        self.scoreboard_width = 800
        self.scoreboard_height = 50
    
    def change_bullet_setting(self, setting):
        # Change the bullet setting
        self.bullet_speed, self.bullet_width, self.bullet_height = self.bullet_setting[setting]
