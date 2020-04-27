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
        # life
        self.life = 4
        # if the player is inflicted with damage, it cannnot be inflicted again for a certain amount of time
        self.life_lost_time = 0

    # movements
    def update(self,event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.move_right = True
            if event.key == pygame.K_LEFT:
                self.move_left = True
            if event.key == pygame.K_UP:
                self.move_up = True
            if event.key == pygame.K_DOWN:
                self.move_down = True
            if event.key == pygame.K_SPACE:
                self.immunity = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.move_right = False
            if event.key == pygame.K_LEFT:
                self.move_left = False
            if event.key == pygame.K_UP:
                self.move_up = False
            if event.key == pygame.K_DOWN:
                self.move_down = False