import pygame
from pygame.sprite import Group

from settings import Settings

from ship import Ship

<<<<<<< HEAD
from alien import Alien

=======
>>>>>>> a7cbc524b244db6caef9632c11c617e6efb52db1
import game_functions as gf

def run_game():
    #Initialize pygame,settings and screen object
    pygame.init()
    ai_settings =Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #makes a ship
    ship = Ship(ai_settings,screen)

<<<<<<< HEAD
    #Make an alien
    alien = Alien(ai_settings,screen)

    #Make a group to store bullets and a group for aliens
    bullets = Group()
    aliens = Group()

    #Create the fleetof aliens
    gf.create_fleet(ai_settings,screen,aliens)
=======
    #Make a group to store bullets in
    bullets = Group()
>>>>>>> a7cbc524b244db6caef9632c11c617e6efb52db1

    #start the main loop for the game
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
<<<<<<< HEAD
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
=======
        gf.update_screen(ai_settings,screen,ship,bullets)
>>>>>>> a7cbc524b244db6caef9632c11c617e6efb52db1

run_game()
