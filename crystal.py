import pygame
from pygame.sprite import Sprite
from random import randint


class Crystal(Sprite):
    def __init__(self, dragons_game):
        super(Crystal, self).__init__()
        self.screen = dragons_game.screen
        self.image = pygame.image.load('images/crystal.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.random_number = randint(-10, 10)
