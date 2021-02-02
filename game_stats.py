class GameStats:

    def __init__(self, dragon_game):
        """
        Инициализирует статистику
        """
        self.settings = dragon_game.settings
        self.reset_stats()
        # Активное состояние игры (делается, чтобы завершить игру при hero_lives = 0)
        self.game_active = False

        # Рекорд очков
        self.score = 0

    def reset_stats(self):
        """
        Инициализирует статистику, изменяющуюся в ходе игры
        """
        self.lives_left = self.settings.hero_lives
        self.score = 0
