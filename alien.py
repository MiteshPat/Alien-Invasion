import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # class to represent single alien in fleet

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load alien and set it's rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        # move alien to the right
        self.x += self.settings.alien_speed
        self.rect.x = self.x