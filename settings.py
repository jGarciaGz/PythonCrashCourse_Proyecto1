class Settings():
    """Clase para guardar los ajustes para el juego """

    def __init__(self):
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
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Configuracion de aliens
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction = 1 representa derecha; -1 representa izquierda
        self.fleet_direction = 1



    
    