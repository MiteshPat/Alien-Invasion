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

        # start each new alien near the top of the screen           2540 1440
        self.rect.x = (self.rect.width)
        self.rect.y = (self.rect.height)

        # store alien's exact diagonal position
        self.y = float(self.rect.y)

    def check_edges(self):
        # return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)

    def update(self):
        # move alien to the right or left
        self.y -= self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y