import pygame.font
from pygame.sprite import Group
from heart import Heart

class Scoreboard:
    """
    Класс для вывода игровой информации
    """
    def __init__(self, dragons_game):
        """
        Атрибуты подсчета очков
        """
        self.dragons_game = dragons_game
        self.screen = dragons_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dragons_game.settings
        self.stats = dragons_game.stats

        # Настройка шрифта для вывода счета
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)

        # Подготовка исходного изображения очков и рекордов очков
        self.prep_score()

        # Сообщает количество оставшихся кораблей(жизней)
        self.prep_lives()

    def prep_score(self):
        """
        Преобразует текущий счет в гарфическое изображение
        """
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.background_color)

        # Вывод счета справа сверху
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """
        Выводит счет, рекорд, уровень и жизни корабля
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.lives.draw(self.screen)

    def prep_lives(self):
        """
        Сообщает количество оставшихся кораблей(жизней)
        """
        self.lives = Group()
        for life_number in range(self.stats.lives_left):
            life = Heart(self.dragons_game)
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = 10
            self.lives.add(life)
