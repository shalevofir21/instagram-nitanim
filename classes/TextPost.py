import pygame

from classes.Post import Post
from constants import POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT, \
    TEXT_POST_FONT_SIZE
from helpers import from_text_to_array, screen, center_text


class TextPost(Post):
    def __init__(self, location, description, text, text_color,
                 background_color):
        Post.__init__(self, location, description)
        self.background_color = background_color
        self.text_color = text_color
        self.text_array = from_text_to_array(text)

    def display_content(self):
        pygame.draw.rect(screen, self.background_color,
                         pygame.Rect(POST_X_POS,
                                     POST_Y_POS,
                                     POST_WIDTH,
                                     POST_HEIGHT))
        for i in range(0, len(self.text_array)):
            text_font = pygame.font.SysFont('chalkduster.ttf',
                                            TEXT_POST_FONT_SIZE, bold=False)
            text_to_display = text_font.render(self.text_array[i],
                                               True, self.text_color)
            text_pos = center_text(len(self.text_array), text_to_display, i)
            screen.blit(text_to_display, text_pos)