import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Inicializar la nave y ponerla en la posicion inicial"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
        #Guardar un valor decimal para el centro de la nave
        self.center = float(self.rect.centerx)

        #Bandera de movimeinto a la derecha
        self.moving_right = False
        #Bandera de movimeinto a la izquierda
        self.moving_left = False


    def update(self):
        """Actulizar la nave en base a la bandera de movimiento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        #Actualizar el objeto rect de self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Dibujar la nave y su ubicacion """
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Centrar la nave"""
        self.center = self.screen_rect.centerx