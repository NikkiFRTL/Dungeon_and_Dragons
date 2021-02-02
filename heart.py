import pygame
from pygame.sprite import Sprite


class Heart(Sprite):
    def __init__(self, dragons_game):
        super(Heart, self).__init__()
        self.screen = dragons_game.screen
        self.image = pygame.image.load('images/heart.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
