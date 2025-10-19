## @last-modified: 12:56 19/10/25
## | Renamed to globals.py as to avoid using too many arbitrary files.

#This exists to avoid a circular import
import pygame
import os

image_types = ['.png']

cwd = os.getcwd()
win = pygame.display.set_mode((0,0),0,pygame.FULLSCREEN)

def Assets():
    files = os.listdir(os.path.join(cwd, 'assets'))
    preloadedAssets = {}

    for file in files:
        path, ext = file.split(os.path.extsep)
        path=os.path.basename(path)

        if ext in image_types:
            preloadedAssets[path] = pygame.image.load(file)
    return preloadedAssets