
import pygame

class Ship:
    def __init__(self, ai_game):

        #initalize ship and starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at bottom center of screen
        self.rect.center = self.screen_rect.center
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movementflag
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
        #update ship based on movement flag
        #update ship's x value not the rect
        print(self.rect.top)
        print(self.screen_rect.top)
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed 
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image, self.rect)