import sys

import pygame

def check_events():
    """Responde a las teclas y clicks del mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Actulizar lo que pasa en la pantalla"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()