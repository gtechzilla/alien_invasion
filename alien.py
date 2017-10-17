import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class representing an alien in the fleet"""
    def __init__(self,ai_settings,screen):
        """Initializethe alien andsetits starting position"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien image and set its rect attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near the top of the screen.
        self.rect.x =self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the alien at its current location"""
        self.screen.blit(self.image,self.rect)
