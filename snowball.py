import pygame
from pygame.sprite import Sprite


class Snowball(Sprite):

    def __init__(self, dragons_game):
        super().__init__()
        self.screen = dragons_game.screen
        self.settings = dragons_game.settings
        self.screen_rect = dragons_game.screen.get_rect
        self.image = pygame.image.load('images/snowball.png')
        self.rect = self.image.get_rect()
        # начальное расположение
        self.rect.midleft = dragons_game.hero.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.snowball_speed
        self.rect.x = self.x

    def blit_snowball(self):
        self.screen.blit(self.image, self.rect)
