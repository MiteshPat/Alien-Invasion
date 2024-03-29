import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self, ai_game):
        
        # initalize ship and starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # movementflag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update ship based on movement flag
        # update ship's x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        # draw ship at current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # center ship on screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)