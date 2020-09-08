import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Inicio del juego y creacion de la pantalla del juego
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    #Inicio del ciclo del juego
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
        

if __name__ == "__main__":
    run_game()