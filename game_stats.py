class GameStats():
    """Seguir las estadisticas de Alien Invasion"""

    def __init__(self, ai_settings):
        """Inicializar las estadisticas"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Empezar Alien Invasion en un estado inactivo
        self.game_active = False

    def reset_stats(self):
        """Inicializar las estadisticas que puden cambiar durante el juego"""
        self.ships_left = self.ai_settings.ship_limit
