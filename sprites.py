import pygame
from constants import *
import numpy as np
from constants import *

class SpriteSheet(object):
    def __init__(self):
        self.sheet = pygame.image.load("spriteSheet.png").convert()
        transcolor = self.sheet.get_at((0,0))
        self.sheet.set_colorkey(transcolor)
        width = int(self.sheet.get_width() / BASETILEWIDTH * TILEWIDTH)
        height = int(self.sheet.get_height() / BASETILEHEIGHT * TILEHEIGHT)
        self.sheet = pygame.transform.scale(self.sheet, (width, height))

    def getImage(self, x, y, width, height):
        x *= TILEWIDTH
        y *= TILEHEIGHT
        self.sheet.set_clip(pygame.Rect(x, y, width, height))
        return self.sheet.subsurface(self.sheet.get_clip())


class PacmanSprites(SpriteSheet):
    def __init__(self, entity):
        SpriteSheet.__init__(self)
        self.entity = entity
        self.entity.image = self.getStartImage()

    def getStartImage(self):
        return self.getImage(8, 0)

    def getImage(self, x, y):
        return SpriteSheet.getImage(self, x, y, 2*TILEWIDTH, 2*TILEHEIGHT)


class GhostSprites(SpriteSheet):
    def __init__(self, entity):
        SpriteSheet.__init__(self)
        self.x = {BLINKY: 0, PINKY: 2, INKY: 4, CLYDE: 6}
        self.entity = entity
        self.entity.image = self.getStartImage()

    def getStartImage(self):
        return self.getImage(self.x[self.entity.name], 4)

    def getImage(self, x, y):
        return SpriteSheet.getImage(self, x, y, 2 * TILEWIDTH, 2 * TILEHEIGHT)

class FruitSprites(SpriteSheet):
    def __init__(self, entity):
        SpriteSheet.__init__(self)
        self.entity = entity
        self.entity.image = self.getStartImage()

    def getStartImage(self):
        return self.getImage(16, 8)

    def getImage(self, x, y):
        return SpriteSheet.getImage(self, x, y, 2*TILEWIDTH, 2*TILEHEIGHT)

class LIfeSprites(SpriteSheet):
    def __init__(self, numlives):
        SpriteSheet.__init__(self)
        self.resetLives(numlives)

    def removeImage(self):
        if len(self.images) > 0:
            self.images.pop(0)

    def resetLives(self, numlives):
        self.images = []
        for i in range(numlives):
            self.images.append(self.getImage(0,0))

    def getImage(self, x, y):
        return SpriteSheet.getImage(self, x, y, 2*TILEWIDTH, 2*TILEHEIGHT)

class MazeSprites(SpriteSheet):
    def __init__(self, mazefile, rotfile):
        SpriteSheet.__init__(self)
        self.data = self.readMazeFile(mazefile)
        self.rotdata = self.readMazeFile(rotfile)

    def getImage(self, x, y):
        return SpriteSheet.getImage(self, x, y, TILEWIDTH, TILEHEIGHT)

    def readMazeFile(self, mazefile):
        return np.loadtxt(mazefile, dtype='<U1')

    def constructBackground(self, background, y):
        for row in list(range(self.data.shape[0])):
            for col in list(range(self.data.shape[1])):
                if self.data[row][col].isdigit():
                    x = int(self.data[row][col]) + 12
                    sprite = self.getImage(x, y)
                    rotval = int(self.rotdata[row][col])
                    sprite = self.rotate(sprite, rotval)
                    background.blit(sprite, (col*TILEWIDTH, row*TILEHEIGHT))
                elif self.data[row][col] == '=':
                    sprite = self.getImage(10, 8)
                    background.blit(sprite, (col*TILEWIDTH, row*TILEHEIGHT))

        return background

    def rotate(self, sprite, value):
        return pygame.transform.rotate(sprite, value*90)


