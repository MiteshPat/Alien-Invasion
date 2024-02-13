
import pygame

class Ship:
    def __init__(self, ai_game):

        #initalize ship and starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #movementflag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update ship based on movement flag
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image, self.rect)