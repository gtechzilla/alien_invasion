import sys

import pygame

from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """Responds to key presses"""
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True
    elif event.key ==pygame.K_LEFT:
        #moves ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    #creates a bullet and adds it to bullet group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """Responds to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """responds to keypresses and mouse events"""

    #Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        #moves ship depending on the arrow key pressed
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        #stops movement of the ship when a pressed arrow key is released
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship,bullets):
    """Update images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)
    #Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()


    #Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """Updates bullet position and rids of old bullets"""
    #getting ridof bullets that reach top of the window(screen)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
