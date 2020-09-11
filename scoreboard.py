import pygame.font

class Scoreboard():
    """Una clase para llevar la informacion del puntaje"""
    def __init__(self, ai_settings, screen, stats):
        """Inicializar los atributos del puntaje"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #Configuracion de la fuente para el puntaje
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #Preparar la imagen del puntaje incial
        self.prep_score()

    def prep_score(self):
        """"Convertir el puntaje en una imagen"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
        #Mostrar el puntaje en la esquina superior derecha  de la pantalla
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Poner el puntaje en la pantalla"""
        self.screen.blit(self.score_image, self.score_rect)