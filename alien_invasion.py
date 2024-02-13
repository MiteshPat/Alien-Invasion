import sys
import pygame
from settings import Settings

class AlienInvasion():

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        # game runs at a certain frame time 

       
        pygame.display.set_caption("Alien Invasion")
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
      
    
    def run_game(self):
        # start main loop of game
        while True:
            # watch for keyboard/mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)

            #fills screen during each pass of loop

            # make most recently drawn screen visibile 
            pygame.display.flip()
            self.clock.tick(60)
            # runs at 60 frames


if __name__ == '__main__':
        # make a game instance and run the game
        ai = AlienInvasion()
        ai.run_game()