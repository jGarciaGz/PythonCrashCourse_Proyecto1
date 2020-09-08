import pygame

class Ship():
    def __init__(self, screen):
        """Inicializar la nave y ponerla en la posicion inicial"""
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        """Dibujar la nave y su ubicacion """
        self.screen.blit(self.image, self.rect)