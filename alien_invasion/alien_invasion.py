import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    #draws a ship
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    #MY BACKGROUND COLOUR
    while True:
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)
run_game()
