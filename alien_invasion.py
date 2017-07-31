import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings=Settings()
    #draws a ship
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    #where bullets are stored
    bullets =Group()
    #MY BACKGROUND COLOUR
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()
