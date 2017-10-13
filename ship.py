import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ships image
        self.image=pygame.image.load('images/ship.bmp')

        #used to access the surface(image) rectangular attributes
        self.rect=self.image.get_rect()

        #used to obtain the screens rectangular attributes
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        #assigns center of ships surface to center of screen surface
        self.rect.centerx = self.screen_rect.centerx
        #assigns the bottom y coordinate of the ships surface to the screens bottom y coordinate
        self.rect.bottom = self.screen_rect.bottom

        #stores a decimal value for the ships center
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the position of ship when flag is set to true"""
        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.center +=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -=self.ai_settings.ship_speed_factor

        #updates the rect object from self.center
        self.rect.centerx =self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)
