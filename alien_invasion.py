import sys
import pygame

class AlienInvasion():

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        # game runs at a certain frame time 

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        # start main loop of game
        while True:
            # watch for keyboard/mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)

            #fills screen during each pass of loop

            # make most recently drawn screen visibile 
            pygame.display.flip()
            self.clock.tick(60)
            # runs at 60 frames


if __name__ == '__main__':
        # make a game instance and run the game
        ai = AlienInvasion()
        ai.run_game()