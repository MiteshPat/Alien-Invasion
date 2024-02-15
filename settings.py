
class Settings:
    # store settings for Alien Invasion

    def __init__(self):
        # self.screen_width = 1200
        # self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        
        # bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 15
        self.bullet_height = 300
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # alien settings
        self.alien_frequency = 0.015
        self.alien_speed = 6.0

        # ship settings
        self.ship_speed = 5.0
        self.ship_limit = 3