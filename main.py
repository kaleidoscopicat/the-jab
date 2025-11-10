import os
import random


from game.classes import Player, screen_object, Floor, Present
from game.globals import win, Assets

try:
    import pygame
except ModuleNotFoundError as e:
    os.system("pip install pygame --user")

pygame.display.set_caption("Present catcher")
run = True

pygame.init()

preloaded_images = Assets()

screen_objects = [Player(500,500, preloaded_images["player"]),
                  Floor(0,600,preloaded_images["floor"]),
                  Floor(500,600,preloaded_images["floor"]),
                  Present(random.randint(0,1000), 0, 5, preloaded_images["present"])
                  ]
presents = []

score = 0
score_font = pygame.font.SysFont("comic_sans", 30)
score_text = score_font.render(f"Score: {score}", True, (255,0,0))

while run:
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        run = False

    win.fill((0,0,0))

    score_text = score_font.render(f"Score: {score}", True, (255, 0, 0))
    win.blit(score_text, (80,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    presents = [present for present in screen_objects if isinstance(present, Present)]
    floors_that_presents_care_about = [floor for floor in screen_objects if isinstance(floor, Floor)]

    if pygame.mouse.get_pressed()[0]:
        screen_objects.append(Present(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 5, preloaded_images["present"]))

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

                #present collisions
                for present in presents:
                    if present.hitbox.colliderect(obj.hitbox):
                        screen_objects.remove(present)
                        screen_objects.append(Present(random.randrange(0,1000),0, 5, preloaded_images["present"]))
                        score += 1

            if isinstance(obj, Present):

                for floor in floors_that_presents_care_about:

                    if obj.hitbox.colliderect(floor.hitbox):
                        obj.falling = False
                        break

    pygame.display.update()
pygame.quit()