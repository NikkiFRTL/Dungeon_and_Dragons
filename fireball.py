import pygame
from pygame.sprite import Sprite


class Fireball(Sprite):

    def __init__(self, dragons_game):
        super().__init__()
        self.screen = dragons_game.screen
        self.settings = dragons_game.settings
        self.screen_rect = dragons_game.screen.get_rect
        self.image = pygame.image.load('images/fireball1.png')
        self.rect = self.image.get_rect()
        # начальное расположение
        self.rect.midleft = dragons_game.hero.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.fireball_speed
        self.rect.x = self.x

    def blit_fireball(self):
        self.screen.blit(self.image, self.rect)
