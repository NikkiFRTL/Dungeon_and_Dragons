import pygame


class Hero:

    def __init__(self, dragons_game):
        self.screen = dragons_game.screen
        self.screen_rect = dragons_game.screen.get_rect()
        self.image = pygame.image.load('images/hero.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)
