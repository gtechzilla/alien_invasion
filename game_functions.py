import sys
import pygame
from bullets import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #detects when the left or right arrow key is realeased
    if event.key == pygame.K_RIGHT:
        '''condition when the right arrow key is pressed'''
        ship.moving_right = True
    #checks when left arrow key is pressed
    elif event.key == pygame.K_LEFT:
        #when pressed it assigns it a true value
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #creates new bullet in the bullets group
        fire_bullets(ai_settings,screen,ship,bullets)
def fire_bullets(ai_settings,screen,ship,bullets):
    #fires a bullet if limit is not exceeded
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet =Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
def check_keyup_events(event,ship):
    #detects when the left or right arrow key is realeased
    if event.key == pygame.K_RIGHT:
        #when right key is released the condition is set to a false state
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        #when right key is released the condition is set to a false state
        ship.moving_left = False
def check_events(ai_settings,screen,ship,bullets):
    #monitors input from keyboard or mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            '''exits the game when user clicks exit'''
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            '''detects when a key is pressed on the keyboard'''
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        #checks when the key is released
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship,bullets):
    #updates images on the screen and switchs to the updated screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #draws bullets to the screen
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

def update_bullets(bullets):
    #updates position of bullets and rids old bullets
    bullets.update()

    #deletes bullets that have reched the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
