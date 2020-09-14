class Settings():
    """Clase para guardar los ajustes para el juego """

    def __init__(self):
        """Inicializando las estadisticas estaticas del juego"""
        #Configuracion de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #Configuracion de la nave
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        #Configuracion de las balas
        self.bullet_speed_factor = 2
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 220,20,60
        self.bullets_allowed = 3

        #Configuracion de aliens
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction = 1 representa derecha; -1 representa izquierda
        self.fleet_direction = 1

        #Que tan rapido el juego aumenta de velocidad
        self.speedup_scale = 1.1
        #Que tan rapido aumenta el valor de los puntos
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicilizar las configuraciones que cambian durante el juego"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        #Puntos
        self.alien_points = 50

    def increase_speed(self):
        """Incrementar la configuracion de velocidad y valor de los puntos"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)