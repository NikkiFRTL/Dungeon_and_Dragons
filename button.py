import pygame.font


class Button:

    def __init__(self, ai, message):
        """
        Инициализирует атрибут кнопки
        """
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств кнопок
        self.width, self.height = 200, 50
        self.button_color = (0, 250, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки сохлается только 1 раз
        self._prep_message(message)

    def _prep_message(self, message):
        """
        Преобразует message в прямоугольник и выравнивает текст по центру
        """
        self.message_image = self.font.render(message, True, self.text_color, self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        # Отображение пустой кнопки и вывод сообщения
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
