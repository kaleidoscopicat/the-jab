import os
import time

from game.classes import Player, screen_object, Floor
from game.globals import win, Assets

try:
    import pygame
except ModuleNotFoundError as e:
    os.system("pip install pygame --user")

pygame.display.set_caption("Present catcher")
run = True

preloaded_images = Assets()

screen_objects = [Player(500,500, preloaded_images["player"]),
                  Floor(0,600,preloaded_images["floor"]),
                  Floor(500,500,preloaded_images["floor"])
                  ]

while run:
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        run = False

    win.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for obj in screen_objects:
        if isinstance(obj, screen_object):
            obj.update()

            if isinstance(obj, Player):
                obj.on_floor = False
                obj.falling = True

                #Floor collision - may need improvement later but idrc rn
                for floor in screen_objects:

                    if isinstance(floor, Floor) and obj.hitbox.colliderect(floor.hitbox):
                            obj.falling = False
                            obj.on_floor = True
                            break


    pygame.display.update()
pygame.quit()