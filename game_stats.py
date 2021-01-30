class GameStats:

    def __init__(self, dragon_game):
        """
        Инициализирует статистику
        """
        self.settings = dragon_game.settings
        self.reset_stats()
        # Активное состояние игры (делается, чтобы завершить игру при ships_left = 0)
        self.game_active = False

    def reset_stats(self):
        """
        Инициализирует статистику, изменяющуюся в ходе игры
        """
        self.lives_left = self.settings.hero_lives