import pygame

class Ship():

    def __init__(self,ai_settings,screen):
      '''initialize the ship and set its starting position'''
      self.screen = screen
      self.ai_settings = ai_settings

      #Ships image and its rectangle
      self.image = pygame.image.load('images/ship.bmp')
      self.rect = self.image.get_rect()
      self.screen_rect = screen.get_rect()
      #initial position of the ship at the begining of the game
      #initial position of the ship at the begining of the game
      self.rect.centerx = self.screen_rect.centerx
      self.rect.bottom = self.screen_rect.bottom
      self.center = float(self.rect.centerx)

      #for moving the ship tothe right
      self.moving_right = False
      self.moving_left = False
    def update(self):
      #moves the ship within the described limits
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center




    def blitme(self):
      #shows ship at its current location
      self.screen.blit(self.image,self.rect)
