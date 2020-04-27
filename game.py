# -*- coding: utf-8 -*-

import pygame
import sys
import random
import numpy as numpy
import datetime

CLOUD_VELOCITY = 4
CLOUD_JUMP = 20
COLORS = [[255, 0, 0], [255, 165,0], [255, 255, 0], [0, 255, 0], [0, 0, 255], [128, 0, 128]]

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Cloud Jump the Rope")
heart_image = pygame.image.load("images/heart.png")
clock = pygame.time.Clock()

class Cloud:
    def __init__(self, x, y):
        # position
        self.x = x
        self.y = y

        # image before scaling
        self.rough_image = pygame.image.load("images/cloud.png").convert()
        # properly scaled image
        self.image = pygame.transform.scale(self.rough_image, (20, 20))
        # image to show when the player is jumping
        self.immune_image = pygame.transform.scale(self.rough_image, (30, 30))
        # about movements
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        # if jumping or not
        self.immunity = False
        # the player cannot jump more than a specified amount of time
        self.immunity_count = 0
        