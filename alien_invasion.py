import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Inicio del juego y creacion de la pantalla del juego
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Creacion de la nave
    ship = Ship(ai_settings, screen)
    #Crear un grupo de balas
    bullets = Group()

    #Inicio del ciclo del juego
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        

if __name__ == "__main__":
    run_game()