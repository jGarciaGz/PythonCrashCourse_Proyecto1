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
    
        #Bandera de movimeinto a la derecha
        self.moving_right = False
        #Bandera de movimeinto a la izquierda
        self.moving_left = False


    def update(self):
        """Actulizar la nave en base a la bandera de movimiento"""
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Dibujar la nave y su ubicacion """
        self.screen.blit(self.image, self.rect)