import pygame
from constants import *
from constants import NUM_OF_COMMENTS_TO_DISPLAY, COMMENT_TEXT_SIZE, \
    VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS
from helpers import screen
from classes.Comment import Comment

class Post:
    user_name = "Shalev ofir"
    def __init__(self,  location, description):
        self.location = location
        self.description = description
        self.counter_likes = 0
        self.comments = []
        self.comments_display_index = 0
    def display(self):
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()
    def display_content(self):
        pass

    def display_header(self):
        location_font = pygame.font.SysFont('chalkduster.ttf', 15)
        location_to_display = location_font.render(self.location, True, (134, 134, 134))
        screen.blit(location_to_display, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))
        description_font = pygame.font.SysFont('chalkduster.ttf', 15)
        description_to_display = description_font.render(self.description, True, (50, 50, 50))
        screen.blit(description_to_display, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))
        user_name_font = pygame.font.SysFont('chalkduster.ttf', 15,bold=True)
        user_name_to_display = user_name_font.render(self.user_name, True, (50, 50, 50))
        screen.blit(user_name_to_display, (USER_NAME_X_POS, USER_NAME_Y_POS))

    def display_likes(self):
        likes_font = pygame.font.SysFont('chalkduster.ttf', 15)
        likes_to_display = likes_font.render("liked by " + str(self.counter_likes) + " users", True, (0, 0, 0))
        screen.blit(likes_to_display, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))
    def add_like(self):
        self.counter_likes += 1
    def add_comment(self,read_comment_from_user):
        r = Comment(read_comment_from_user)
        self.comments.append(r)
    def display_comments(self):
        position_index = self.comments_display_index
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            comment_to_display = comment_font.render("view more comments",
                                                     True, (134, 134, 134))
            screen.blit(comment_to_display, (VIEW_MORE_COMMENTS_X_POS,
                                             VIEW_MORE_COMMENTS_Y_POS))

        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break
