import pygame


class Hero:
    """
    Создание класа Hero содержащий его поведение
    """
    def __init__(self, dragons_game):
        self.screen = dragons_game.screen
        self.settings = dragons_game.settings
        self.screen_rect = dragons_game.screen.get_rect()
        self.image = pygame.image.load('images/heroine.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """
        Обновляет позицию Hero с учетом флага (True / False)
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.hero_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.hero_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.hero_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.hero_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blit_hero(self):
        self.screen.blit(self.image, self.rect)

    def center_hero(self):
        """
        Размещает героя в начальной позиции после потери жизни
        """
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
