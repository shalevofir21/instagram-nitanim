import pygame

from classes.Button import Button
from test_methods import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from helpers import screen
from buttons import like_button
from buttons import comment_button
from buttons import click_post_button
from classes.ImagePost import ImagePost
from classes.TextPost import *
def main():
    pygame.init()

    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    img_path = "images/background.png"
    img = pygame.image.load(img_path)

    img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))

    screen.blit(img, (0, 0))
    post = ImagePost("images/ronaldo.jpg", "israel", "hello israel")
    post2 = ImagePost("images/dog.jpg", "israel", "hi !")
    post3 = ImagePost("images/cat.jpg", "israel", " im cat !")
    text_post = TextPost("israel","hello text","text text text", (50,200,40),(50,50,50))
    post_list = [post, post2, post3,text_post]
    current_index = 0
    current_post = post_list[current_index]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if mouse_in_button(like_button, pos):
                    current_post.add_like()
                if mouse_in_button(comment_button, pos):
                    comment = read_comment_from_user()
                    current_post.add_comment(comment)
                if mouse_in_button(click_post_button, pos):
                    if current_index == len(post_list) - 1:
                        current_index = 0
                    else:
                        current_index += 1
                    current_post = post_list[current_index]

        screen.blit(img, (0, 0))
        current_post.display()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


main()
