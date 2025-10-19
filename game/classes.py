## @last-modified: 12:59 19/10/25
## | Merged 'classes' directory into classes.py

import pygame
from game.globals import win
from game.helpers.ImageHelper import generate_hitbox


class screen_object(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite, has_spritesheet = False, sprite_index: int =None):
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.sprite = sprite
        self.has_spritesheet = has_spritesheet
        self.sprite_index = sprite_index

    def update(self):
        self.draw()

    def draw(self):
        if self.has_spritesheet is False:
            win.blit(self.sprite,(self.x,self.y))

        elif self.has_spritesheet is True:
            win.blit(self.sprite[self.sprite_index],(self.x,self.y))

class Player(screen_object):
    def __init__(self, x: float, y: float, sprite, vel=5):
        super().__init__(x, y , sprite)
        self.vel = vel
        self.x: float = x
        self.y: float = y
        self.falling = False
        self.vel_y: float = 0
        self.hitbox = generate_hitbox(self.sprite, self.x, self.y)
        self.on_floor: bool = False

        #Gravity constants
        self.jump_strength: float = -25
        self.max_fall_speed: float = 5
        self.gravity: float = 2

    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.x -= self.vel

        elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.x += self.vel

        if (keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.K_w] or
            keys_pressed[pygame.K_UP]) and self.on_floor:
            self.vel_y = self.jump_strength
            self.on_floor = False


        if self.falling or not self.on_floor:
            self.vel_y += self.gravity

            if self.vel_y > self.max_fall_speed:
                self.vel_y = self.max_fall_speed

            self.y += self.vel_y
        else:
            self.vel_y = 0

        self.hitbox = generate_hitbox(self.sprite, self.x, self.y)
        self.draw()
    
    def draw(self):
        if self.has_spritesheet is False:
            win.blit(self.sprite,(self.x, self.y))

        elif self.has_spritesheet is True:
              win.blit(self.sprite[self.sprite_index],(self.x, self.y))

class Floor(screen_object):
    def __init__(self,x,y,spr):
        super().__init__(x,y,spr,False,None)
        self.hitbox = generate_hitbox(spr, x, y)

    def update(self):
        self.hitbox = generate_hitbox(self.sprite, self.x, self.y)
        self.draw()

    def draw(self):
        win.blit(self.sprite, (self.x, self.y))