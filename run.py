import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from nodes import NodeGroup


class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def startGame(self):
        self.setBackground()
        self.nodes = NodeGroup()
        self.nodes.setupTestNodes()
        self.pacman = Pacman(self.nodes.nodeList[0])

    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)
        self.checkEvents()
        self.render()

    # close the window
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    def render(self):
        self.screen.blit(self.background, (0,0))  # note, if this is canceled out the images appears to smear on screen
        self.nodes.render(self.screen)
        self.pacman.render(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()

"""
the addition of time, is for the calculation of the velocity and finding the new position of the pacman
the render method is used to the images on the screen.
without the checkEvents() method, the window shall not be able to close up
"""
