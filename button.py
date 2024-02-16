import pygame.font

class Button:
    # class to build buttons for the game

    def __init__(self, ai_game, msg):
        # create button attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # set dimensions and properites of button
        self.width, self.height = 200, 50
        self.base_color = (0, 135, 0)
        self.highlighed_color = (0, 65, 0)
        self.msg = msg
        self.button_color = self.base_color
      
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button needs to prepared once
        self._prep_msg()
    
    def _prep_msg(self):
        # turn msg into a rendered image and center text onto the button
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    
    def draw_button(self):
        # draw a blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def _update_msg_position(self):
        self.msg_image_rect.center = self.rect.center

    def set_highlighed_color(self):
        self.button_color = self.highlighed_color
        self._prep_msg

    def set_base_color(self):
        self.button_color = self.base_color
        self._prep_msg()