from classes.Post import Post
import pygame
from constants import *
from constants import NUM_OF_COMMENTS_TO_DISPLAY, COMMENT_TEXT_SIZE, \
    VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS
from helpers import screen


class ImagePost(Post):
    def __init__(self, image_src, location, description):
        Post.__init__(self, location, description)
        img = pygame.image.load(image_src)
        img = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))
        self.image = img

    def display_content(self):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))

