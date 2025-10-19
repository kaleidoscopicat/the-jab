import os

from game.classes import Player, screen_object, Floor
from game.globals import win, Assets

try:
    import pygame
except ModuleNotFoundError as e:
    os.system("pip install pygame --user")

pygame.display.set_caption("Present catcher")
run = True

preloaded_images = Assets()
print(preloaded_images)
player = Player(500,500, preloaded_images["player"])

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

            if isinstance(obj, Player):
                obj.falling = True

                #Floor collision - may need improvement later but idrc rn
                for floor in screen_objects:
                    if isinstance(floor, Floor) and obj.hitbox.colliderect(floor.hitbox):
                            obj.falling = True
                            break

    pygame.display.update()
pygame.quit()