import pygame

class Ship():

    def __init__(self,screen):
      '''initialize the ship and set its starting position'''
      self.screen = screen

      #Ships image and its rectangle
      self.image = pygame.image.load('images/ship.bmp')
      self.rect = self.image.get_rect()
      self.screen_rect = screen.get_rect()

      #initial position of the ship at the begining of the game
      self.rect.centerx = self.screen_rect.centerx
      self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
      #shows ship at its current location
      self.screen.blit(self.image,self.rect)
