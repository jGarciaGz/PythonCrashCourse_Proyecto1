import sys

import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respondiendo a cuando se aprieta una tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        

def check_keyup_events(event, ship):
    """"Respondiendo a cuando se suelta la tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Responde a las teclas y clicks del mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Actulizar lo que pasa en la pantalla"""
    screen.fill(ai_settings.bg_color)
    #Redibujar todas las balas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #alien.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    """Actulizar la posicion de la balas y borrar las viejas"""
    #Actulizar la posicion de la bala
    bullets.update()
    #Borrar las balas que desaparecen de la pantalla
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara una bala si aun no se ha alcanzado el limite permitido"""
    #Creacion de una nueva bala y agregarla al grupo
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
    """Creacion de la flota de aliens"""
    #Crear un alien y encontrar el numero de aliens en fila
    #Espacio entre cada alien es igual a la anchura de un alien
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    #Crear la primera fila de aliens
    for alien_number in range(number_aliens_x):
        #Crear un alien y ponerlo en la fila
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
        

