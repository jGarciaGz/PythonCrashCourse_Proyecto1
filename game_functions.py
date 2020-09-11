import sys
from time import sleep

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

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """Responde a las teclas y clicks del mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, 
                    aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, 
        aliens, bullets, mouse_x, mouse_y):
    """Empezar un nuevo juego cuando le den click en jugar"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #Esconder el cursor
        pygame.mouse.set_visible(False)
        #Resetar las estadisticas del juego
        stats.reset_stats()
        stats.game_active = True 
        #Vacias la lista de los aliens y las balas
        aliens.empty()
        bullets.empty()
        #Crear una nueva flota y centrar la nave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """Actulizar lo que pasa en la pantalla"""
    screen.fill(ai_settings.bg_color)
    #Redibujar todas las balas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #alien.blitme()
    #Dibujar el boton de play si el juego esta inactivo
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Actulizar la posicion de la balas y borrar las viejas"""
    #Actulizar la posicion de la bala
    bullets.update()
    #Borrar las balas que desaparecen de la pantalla
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_aliens_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_aliens_collisions(ai_settings, screen, ship, aliens, bullets):
    """Responder a la colision de balas con aliens"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #Crear una nueva flota te aliens si ya no hay
    if len(aliens) == 0:
        #Destruye las balas existentes y crea una flota de aliens
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara una bala si aun no se ha alcanzado el limite permitido"""
    #Creacion de una nueva bala y agregarla al grupo
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    """Creacion de la flota de aliens"""
    #Crear un alien y encontrar el numero de aliens en fila
    #Espacio entre cada alien es igual a la anchura de un alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #Crear la primera fila de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    """Determinar el numero de aliens que caben en una fila"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Crear un alien y colocarlo en la fila"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determinar el numero de filas de aliens que caben en la pantalla"""
    available_space_y = (ai_settings.screen_height - (10 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respuesta a la colision de nave y alien"""
    if stats.ships_left > 0:
        #Restar una vida
        stats.ships_left -= 1
        #Vaciar la lista de los aliens y las balas
        aliens.empty()
        bullets.empty()
        #Crear una flota y centrar la nave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #Pausa
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Checar si algun alien ha llegado al limte inferior de pantalla"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Haremos lo mismo que si hubiera golpeado la nave (-1 vida)
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Checa si la flota esta en el borde, 
    y luego actuliza la posicion de todos los aliens de la flota"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #Buscar colisiones alien-nave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    #Buscar aliens llegando al limite inferior de la pantalla
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """Responde apropiedamente si algun alien ha llegado al borde"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Baja la flota entera y la cambia de direccion"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
