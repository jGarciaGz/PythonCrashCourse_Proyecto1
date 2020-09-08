import sys

import pygame

def check_keydown_events(event, ship):
    """Respondiendo a cuando se aprieta una tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """"Respondiendo a cuando se suelta la tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Responde a las teclas y clicks del mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """Actulizar lo que pasa en la pantalla"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()