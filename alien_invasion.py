import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #Inicio del juego y creacion de la pantalla del juego
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Crear el boton de play
    play_button = Button(ai_settings, screen, "Play")
    #Crear la instancia para guardar las estadisticas del juego
    stats = GameStats(ai_settings)
    #Crear alien
    alien = Alien(ai_settings, screen)

    #Creacion de la nave
    ship = Ship(ai_settings, screen)
    #Crear un grupo de balas
    bullets = Group()
    #Grupo de aliens
    aliens = Group()

    #Creacion de la flota de aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Inicio del ciclo del juego
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        if stats.game_active:  
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

if __name__ == "__main__":
    run_game()