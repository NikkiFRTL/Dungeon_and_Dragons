import pygame
import sys
from time import sleep
from settings import Settings
from hero import Hero
from fireball import Fireball
from crystal import Crystal
from random import randint
from dragon import Dragon
from snowball import Snowball
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class DungeonAndDragons:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Dungeon and Dragons')
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.stats = GameStats(self)  # Создание экземпляра для хранения игровой статистики
        self.hero = Hero(self)
        self.dragon = Dragon(self)
        self.fireballs = pygame.sprite.Group()
        self.snowballs = pygame.sprite.Group()
        self.crystals = pygame.sprite.Group()
        self.dragons = pygame.sprite.Group()
        self._create_crystals()  # TODO Сделать так, чтобы повялялись новые кристаллы когда все пять фаерболов будет
        # выпущено в дракона
        # Создание кнопки Play
        self.play_button = Button(self, 'Play')
        self.scoreboard = Scoreboard(self)

    def run_game(self):
        """
        Запуск основного цикла игры
        """
        while True:
            self._check_events()
            # Отделим части игры, которые должны выподлняться только при активной игре (game_active = True)
            if self.stats.game_active:
                self.hero.update()
                self._update_snowballs()
                self._update_fireballs()
                self._update_dragon()
                self._update_crystals()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """
        Запускает новую игру при нажатии кнопки Play
        """
        # Проверяет находится ли точка щелчка в пределах прямоугольника
        # и отмена реакции клика по квадрату, если игра активна
        mouse_on_play = self.play_button.rect.collidepoint(mouse_pos)
        if mouse_on_play and not self.stats.game_active:
            # Сброс игровой статистики
            self.stats.reset_stats()
            self.stats.game_active = True

            # Очистка всех списков спрайтов
            self.fireballs.empty()
            self.snowballs.empty()
            self.crystals.empty()

            # Создание и центрирование объектов заного
            self._create_crystals()
            self.dragon.center_dragon()
            self.hero.center_hero()
            self.scoreboard.prep_score()
            self.scoreboard.prep_lives()

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
            self.release_snowball()

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

    def release_snowball(self):
        if len(self.snowballs) < self.settings.snowball_allowed and self.settings.crystals_stack == 3:
            new_snowball = Snowball(self)
            self.snowballs.add(new_snowball)
            self.settings.crystals_stack = 0

    def _update_snowballs(self):
        self.snowballs.update()
        for snowball in self.snowballs.copy():
            if snowball.rect.right >= self.screen.get_rect().right:
                self.snowballs.remove(snowball)
        self._check_snowball_dragon_collision()

    def _check_snowball_dragon_collision(self):
        """
        Обработка коллизий снежных шаров и дракона
        """
        collision = pygame.sprite.spritecollideany(self.dragon, self.snowballs)
        if collision:
            self._dragon_hit()

    def release_fireball(self):
        if len(self.fireballs) < self.settings.fireballs_allowed:
            new_fireball = Fireball(self)
            self.fireballs.add(new_fireball)

    def _update_fireballs(self):
        self.fireballs.update()
        for fireball in self.fireballs.copy():
            if fireball.rect.right <= 0:
                self.fireballs.remove(fireball)
        self._check_fireball_snowball_collision()
        self._check_fireball_hero_collision()

    def _check_fireball_snowball_collision(self):
        """
        Обработка коллизий огненных и снежных шаров
        """
        # Проверка попадений в героя (коллизий) с помощью sprite.groupcollide()
        # True, True обозначает, что нужно удалять каждый объект после столкновения
        collision_fireball_hero = pygame.sprite.groupcollide(self.fireballs, self.snowballs, True, True)

    def _check_fireball_hero_collision(self):
        """
        Обработка коллизий огненных и героя
        """
        if pygame.sprite.spritecollideany(self.hero, self.fireballs):
            self._hero_hit()

    def _update_crystals(self):
        self.crystals.update()
        self._check_hero_crystal_collision()
        if not self.crystals and self.settings.crystals_stack == 0:
            self._create_crystals()

    def _create_crystals(self):
        for row_number in range(1):
            for crystal_number in range(self.settings.crystals_allowed):
                self._create_crystal()

    def _create_crystal(self):
        crystal = Crystal(self)
        crystal.rect.x = randint(50, 1200)
        crystal.rect.y = randint(50, 800)
        if pygame.sprite.collide_rect(self.hero, crystal):
            crystal.rect.x = randint(50, 1200)
            crystal.rect.y = randint(50, 800)
        self.crystals.add(crystal)

    def _check_hero_crystal_collision(self):
        """
        Обработка коллизий героя и кристаллов
        """
        for crystal in self.crystals:
            hero_got_crystal = pygame.sprite.collide_rect(self.hero, crystal)
            if hero_got_crystal:
                self.settings.crystals_stack += 1
                self.crystals.remove(crystal)

    def _check_dragon_edges(self):
        if self.dragon.check_edges():
            self.dragon.x -= self.settings.dragon_drop_speed
            self.settings.dragon_direction *= -1

    def _update_dragon(self):
        self._check_dragon_edges()
        self.dragon.update()
        self._check_dragon_left()  # Проверяет добрался ли дракон до левого края экрана
        self._check_dragon_hero_collision()
        for i in range(3):
            self.release_fireball()

    def _check_dragon_left(self):
        """
        Проверяет добрался ли дракон до левого края экрана
        """
        if self.stats.lives_left > 0:
            screen_rect = self.screen.get_rect()
            for dragon in self.dragons.sprites():
                if dragon.rect.left >= screen_rect.left:
                    # Происхоит тоже, что при столкновении с кораблем
                    self._hero_hit()
                    break
        else:
            self.stats.game_active = False

    def _check_dragon_hero_collision(self):
        if pygame.sprite.spritecollideany(self.hero, self.dragons):
            self._hero_hit()

    def _hero_hit(self):
        """
        Обрабатывает столкнокение дракона с героем
        """
        if self.stats.lives_left > 0:
            # Уменьшение количества жизней на 1
            self.stats.lives_left -= 1
            self.scoreboard.prep_lives()

            # Очистка окна от объектов
            self.fireballs.empty()
            self.snowballs.empty()
            self.dragons.empty()
            self.crystals.empty()
            self.settings.crystals_stack = 0

            # Обновление расположения персонажей учитывая -1 жизнь героя
            self.dragon.center_dragon()
            self.hero.center_hero()
            self._create_crystals()

            # Пауза
            sleep(1)
        else:
            self.stats.game_active = False

    def _dragon_hit(self):
        self.stats.score += 1
        pass

    def _update_screen(self):
        self.screen.fill(self.settings.background_color)

        self.hero.blit_hero()

        self.dragon.blit_dragon()

        for fireball in self.fireballs.sprites():
            fireball.blit_fireball()

        for snowball in self.snowballs.sprites():
            snowball.blit_snowball()

        self.crystals.draw(self.screen)

        # Вывод инфолрмации о счете
        self.scoreboard.show_score()

        # Кнопка Play отображается только когда игра не активна
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    dragons_game = DungeonAndDragons()
    dragons_game.run_game()
