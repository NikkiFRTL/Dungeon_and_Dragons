import pygame
import sys
from settings import Settings
from hero import Hero
from fireball import Fireball
from crystal import Crystal
from random import randint
from dragon import Dragon


class DungeonAndDragons:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Dungeon and Dragons')
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.hero = Hero(self)
        self.dragon = Dragon(self)
        self.fireballs = pygame.sprite.Group()
        self.crystals = pygame.sprite.Group()
        self.dragons = pygame.sprite.Group()
        self._create_crystals()  # TODO Сделать так, чтобы повялялись новые кристаллы когда все пять фаерболов будет
        # выпущено в дракона

    def run_game(self):
        while True:
            self._check_events()
            self.hero.update()
            self._update_fireballs()
            self._update_dragon()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """
        Реагирует на нажатие клавиш.
        """
        if event.key == pygame.K_RIGHT:
            self.hero.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.hero.moving_left = True
        elif event.key == pygame.K_UP:
            self.hero.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.hero.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.release_fireball()

    def _check_keyup_events(self, event):
        """
        Реагирует на отпускание клавиш.
        """
        if event.key == pygame.K_RIGHT:
            self.hero.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.hero.moving_left = False
        elif event.key == pygame.K_UP:
            self.hero.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.hero.moving_down = False

    def release_fireball(self):
        if len(self.fireballs) < self.settings.fireballs_allowed:
            new_fireball = Fireball(self)
            self.fireballs.add(new_fireball)

    def _update_fireballs(self):
        self.fireballs.update()
        for fireball in self.fireballs.copy():
            if fireball.rect.left >= self.screen.get_rect().right:
                self.fireballs.remove(fireball)
        self._check_fireball_dragon_collision()

    def _check_fireball_dragon_collision(self):  # TODO Как в примере с пришельцами(нужен ли спрайт для дракона?)
        collision_fireball_dragon = pygame.sprite.groupcollide(self.fireballs, self.dragons, False, True)
        if not self.dragons:
            self.fireballs.empty()
            dragon = Dragon(self)
            self.dragons.add(dragon)

    def _create_crystals(self):

        for row_number in range(1):
            for crystal_number in range(5):
                self._create_cristal()

    def _create_cristal(self):
        crystal = Crystal(self)
        crystal.rect.x = randint(50, 1200)
        crystal.rect.y = randint(50, 800)
        self.crystals.add(crystal)

    def _check_dragon_edges(self):
        if self.dragon.check_edges():
            self.dragon.x -= self.settings.dragon_drop_speed
            self.settings.dragon_direction *= -1

    def _update_dragon(self):
        self._check_dragon_edges()
        self.dragon.update()

    def _update_screen(self):
        self.screen.fill(self.settings.background_color)

        self.hero.blit_hero()

        self.dragon.blit_dragon()

        for fireball in self.fireballs.sprites():
            fireball.blit_fireball()

        self.crystals.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    dragons_game = DungeonAndDragons()
    dragons_game.run_game()
