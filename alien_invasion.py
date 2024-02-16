import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # game runs at a certain frame time 
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) # call ship after screen to avoid error
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # start alien invasion in active state
        self.game_active = False

        # make play button
        self.play_button = Button(self, "Play")
        self._make_difficulty_buttons()

        self.game_active = False

    def _make_difficulty_buttons(self):

        self.easy_button = Button(self, "Easy")
        self.medium_button = Button(self, "Medium")
        self.hard_button = Button(self, "Hard")

        self.easy_button.rect.top = (
            self.play_button.rect.top + 1.5*self.play_button.rect.height)
        self.easy_button._update_msg_position() 
        
        self.medium_button.rect.top = (
            self.easy_button.rect.top + 1.5*self.easy_button.rect.height)
        self.medium_button._update_msg_position()

        self.hard_button.rect.top = (
            self.medium_button.rect.top + 1.5*self.medium_button.rect.height)
        self.hard_button._update_msg_position()
        
        self.medium_button.set_highlighed_color()

    def _create_fleet(self):
        # create an alien and keep adding until no room left.
        # spacing between aliens is one alien width and one alien height.

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height
        


    def _create_alien(self, x_position, y_position):
        # create an alien and place it on row
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def run_game(self):
        # start main loop of game
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
               
                    # runs at 60 frames
            self.clock.tick(60)
            self._update_screen()

    def _check_events(self):
         # watch for keyboard/mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_difficulty_buttons(mouse_pos)

    def _check_play_button(self, mouse_pos):
        # start a new game when the player clicks play
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
           self._start_game()
           self.stats.reset_stats()
           self.sb._prep_score()
    
    def _check_difficulty_buttons(self, mouse_pos):
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)

        if easy_button_clicked:
            self.settings.difficulty_level = 'easy'
            self.easy_button.set_highlighed_color()
            self.medium_button.set_base_color()
            self.hard_button.set_base_color()
        elif medium_button_clicked:
            self.settings.difficulty_level = 'medium'
            self.medium_button.set_highlighed_color()
            self.easy_button.set_base_color()
            self.hard_button.set_base_color()
        elif hard_button_clicked:
            self.settings.difficulty_level = 'hard'
            self.hard_button.set_highlighed_color()
            self.medium_button.set_base_color()
            self.easy_button.set_base_color()

    def _start_game(self):

        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.game_active = True

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)

                

    def _check_keydown_events(self, event):
        # respond to keypresses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #exit game with keypress q
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.game_active:
            self._start_game()

    def _check_keyup_events(self, event):
        # respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        # create bullet and add it to bullet group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # update position of bullets and get rid of old bullets
        self.bullets.update()

        # check for any bullets that have hit aliens
        # if so, get rid of the bullet and alien
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # respond to bullet-alien collisions
        # remove any bullets and aliens that have collied
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if collisions:
                for aliens in collisions.values():
                    self.stats.score += self.settings.alien_points * len(aliens)
        self.sb._prep_score()
        self.sb.check_high_score()

        if not self.aliens:
            # destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _check_fleet_edges(self):
        # respond if alien reaches edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        # drop entire fleet and change fleet direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        # check if fleet is at edge, then update positons.
        self._check_fleet_edges()
        self.aliens.update()

        # look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _update_screen(self):
         # update images on screen, flip to new screen
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        # draw the play button if game inactive
        if not self.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
        
        pygame.display.flip()

    def _ship_hit(self):
        # respond to ship being hit by alien
        # decrement ships left
        print(self.stats.ships_left)
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

        # get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

        # create new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

        # pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
    

    def _check_aliens_bottom(self):
        # check if any aliens have reached the bottom of the screen
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # treat this the same as ship got hit
                self._ship_hit()
                break

if __name__ == '__main__':
        # make a game instance and run the game
        ai = AlienInvasion()
        ai.run_game()

        