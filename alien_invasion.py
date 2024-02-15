import sys
import pygame
from random import random
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien 
from game_stats import GameStats
class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.stats = GameStats(self)
        self.game_active = True

        # game runs at a certain frame time 
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) # call ship after screen to avoid error
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
     


    def _create_alien(self):
        # create an alien and place it on row
       if random() < self.settings.alien_frequency:
            alien = Alien(self)
            self.aliens.add(alien)
    
    def run_game(self):
        # start main loop of game
        while True:
            self._check_events()
            if self.game_active:
                self._create_alien()

                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
                

    def _check_keydown_events(self, event):
        # respond to keypresses
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        #exit game with keypress q
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # respond to key releases
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        # create bullet and add it to bullet group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # update position of bullets and get rid of old bullets
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                 self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        # respond to bullet-alien collisions
        # remove any bullets and aliens that have collied
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

   

    def _update_aliens(self):
        # check if fleet is at edge, then update positons.
        
        self.aliens.update()

        # look for alien_ship collisions.

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_left()
        
    def _update_screen(self):
         # update images on screen, flip to new screen
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _ship_hit(self):
        # respond to ship being hit by alien
        # decrement ships_left
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            

        # get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

        # create new fleet and center ship
            
            self.ship.center_ship()

        # pause
        else:
            self.game_active = False

    def _check_aliens_left(self):
      
        # check if any aliens have reached the left of the screen
        for alien in self.aliens.sprites():
            if alien.rect.left < 0:
                # treat this the same as ship got hit
                
                self._ship_hit()
                break

if __name__ == '__main__':
        # make a game instance and run the game
        ai = AlienInvasion()
        ai.run_game()

        