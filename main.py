import pygame
import sys
from settings import Settings
from hero import Hero


class DungeonAndDragons:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Dungeon and Dragons')
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.hero = Hero(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.hero.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    dragons_game = DungeonAndDragons()
    dragons_game.run_game()
