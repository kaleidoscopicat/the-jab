import os

from game.classes import player, screen_object
from game.globals import win, Assets

try:
    import pygame
except ModuleNotFoundError as e:
    os.system("pip install pygame --user")

pygame.display.set_caption("Present catcher")
run = True

preloaded_images = Assets()
player = player(500,500, preloaded_images["player"])

_hitbox_cache = {}
screen_objects = []

screen_objects.append(player)

while run:
    win.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for obj in screen_objects:
        if isinstance(obj, screen_object):
            obj.update()

    pygame.display.update()
pygame.quit()