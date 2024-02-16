
class Settings:
    # store settings for Alien Invasion

    def __init__(self):
        
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        
        # bullet settings
        # self.bullet_speed = 10
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        # self.alien_speed = 3
        self.fleet_drop_speed = 50
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #ship settings
        # self.ship_speed = 6.5
        self.ship_limit = 3

        #game settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.difficulty_level = 'medium'
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # settings that can change throughout the game
        if self.difficulty_level == 'easy':
            self.bullets_allowed = 10
            self.ship_limit = 5
            self.ship_speed = 5
            self.bullet_speed = 10
            self.alien_speed = 0.5
            self.alien_points = 25
        
        elif self.difficulty_level == 'medium':
            self.bullets_allowed = 5
            self.ship_limit = 3
            self.ship_speed = 5
            self.bullet_speed = 5
            self.alien_speed = 1
            self.alien_points = 50
           
        elif self.difficulty_level == 'hard':
            self.bullets_allowed = 3
            self.ship_limit = 1
            self.ship_speed = 5
            self.bullet_speed = 3
            self.alien_speed = 1.5
            self.alien_points = 100

        self.fleet_direction = 1
  
    
    def increase_speed(self):
        self.speedup_scale *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def set_difficulty(self, diff_setting):
        if diff_setting == 'easy':
            print('easy')
        elif diff_setting == 'medium':
            pass
        elif diff_setting == 'hard':
            pass


