
class Settings:

    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 900
        self.background_color = (0, 0, 0)

        self.hero_lives = 3
        self.hero_speed = 3

        self.fireball_speed = 2
        self.fireballs_allowed = 3

        self.snowball_speed = 2
        self.snowball_allowed = 1

        self.crystals_allowed = 3
        self.crystals_stack = 0

        self.dragon_speed = 1.0
        self.dragon_drop_speed = 10
        self.dragon_direction = 1
        self.dragon_health = 100
