class Settings():
    #this is our settings class for our game

    def __init__(self):
        #screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #increments the ship position by 1.5 pixels on each pass through the loop
        self.ship_speed_factor = 1.5
        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = 60,60,60
