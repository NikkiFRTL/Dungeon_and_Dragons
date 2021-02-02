import pygame


class Dragon:

    def __init__(self, dragons_game):
        self.screen = dragons_game.screen
        self.settings = dragons_game.settings
        self.screen_rect = dragons_game.screen.get_rect()
        self.image = pygame.image.load('images/dragon.png')
        self.rect = self.image.get_rect()
        # начальное расположение
        self.rect.right = self.screen.get_rect().right
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blit_dragon(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """
        Возвращает True, если дракон находится у края экрана
        """
        screen_rect = self.screen.get_rect()
        if self.rect.bottom > screen_rect.bottom or self.rect.top < 0:
            return True

    def update(self):
        """
        Перемещает пришельца вправо или влево
        """
        self.y += (self.settings.dragon_speed * self.settings.dragon_direction)
        self.rect.y = self.y
        self.rect.x = self.x

    def center_dragon(self):
        """
        Размещает ракона в начальной позиции после потери жизни
        """
        self.rect.midright = self.screen_rect.midright
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
