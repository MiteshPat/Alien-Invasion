import pygame
from random import randint
from pygame.sprite import Sprite

class Alien(Sprite):
    # class to represent single alien in fleet

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load alien and set it's rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        # self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()

        # start each new alien random position right side
        self.rect.left = self.screen.get_rect().right

        # check to ensure doesn't go above height of screen
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)
        self.x = float(self.rect.x)

    def update(self):
        # move alien to the right or left
        self.x -= self.settings.alien_speed
        self.rect.x = self.x