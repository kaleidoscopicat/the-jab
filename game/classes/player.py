import pygame

from game.object import screen_object
from game.win import win

class player(screen_object):
    def __init__(self, x: float, y: float, sprite, vel=5):
        super().__init__(x, y , sprite)
        self.vel = vel
        self.x = x
        self.y = y

    def update(self):

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.x -= self.vel

        elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.x += self.vel

        self.draw()

    def draw(self):
        if self.has_spritesheet is False:
            win.blit(self.sprite,(self.x, self.y))

        elif self.has_spritesheet is True:
              win.blit(self.sprite[self.sprite_index],(self.x, self.y))