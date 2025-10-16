import pygame

from game.win import win


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

