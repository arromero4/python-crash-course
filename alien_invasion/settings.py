class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings"""
        #screen settings
<<<<<<< HEAD
        self.screen_width = 1280
        self.screen_height = 720
=======
        self.screen_width = 840
        self.screen_height = 480
>>>>>>> b93e7e6 (Python Crash Course)
        self.bg_color = (135, 206, 235)

        #Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)