import os

from game.classes.player import player
from game.object import screen_object
from game.win import win

try:
    import pygame
except Exception as e:
    os.system("pip install pygame --user")


pygame.display.set_caption("Present catcher")
run = True
win = win
preloaded_images = [
    pygame.image.load("game/assets/player.png")

]

player = player(500,500, preloaded_images[0])


_hitbox_cache:dict = {}
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