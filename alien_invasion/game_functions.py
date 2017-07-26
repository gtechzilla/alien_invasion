import sys
import pygame

def check_events():
    #monitors input from keyboard or mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(ai_settings,screen,ship):
    #updates images on the screen and switchs to the updated screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
