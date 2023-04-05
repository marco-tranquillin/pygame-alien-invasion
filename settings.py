class Settings:
    """Describe game settings"""

    def __init__(self):
        # Display
        self.caption = "Alien Invasion"
        self.screen_height = 1024
        self.screen_width = 768
        self.bg_color = (230,230,230)
        self.fps = 60

        # Ship
        self.ship_speed = 2.0

        # Bullet
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
