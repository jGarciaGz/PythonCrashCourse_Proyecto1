import sys

import pygame
from settings import Settings
from ship import Ship

def run_game():
    #Inicio del juego y creacion de la pantalla del juego
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    #Inicio del ciclo del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

if __name__ == "__main__":
    run_game()