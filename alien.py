import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Una clase que representa una oleada de aliens"""
    def __init__(self, ai_settings, screen):
        """Crear al alien y fijarle la posicion de inicio"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Cargar la imagen de alien y ponerla en el atributo rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Iniciar cada alien cerca de la esquina superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Guardar la posicion exacta del alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibujar al alien y su posicion actual"""
        self.screen.blit(self.image, self.rect)
    
