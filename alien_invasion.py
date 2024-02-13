import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # game runs at a certain frame time 
        pygame.display.set_caption("AlienInvasion")
        self.ship = Ship(self) # call ship after screen to avoid error
      
    
    def run_game(self):
        # start main loop of game
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    
            self.clock.tick(60)
            # runs at 60 frames

    def _check_events(self):
         # watch for keyboard/mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                

    def _check_keydown_events(self,event):
        # respond to keypresses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        #exit game with keypress q
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        # respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
         #update images on screen, flip to new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
        # make a game instance and run the game
        ai = AlienInvasion()
        ai.run_game()
        

        