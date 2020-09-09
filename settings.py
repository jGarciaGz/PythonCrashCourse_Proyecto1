class Settings():
    """Clase para guardar los ajustes para el juego """

    def __init__(self):
        #Configuracion de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #Configuracion de la nave
        self.ship_speed_factor = 1.5

        #Configuracion de los disparos
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        


    
    