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

# define ropes and dots
class Rope:
    def __init__(self, x = 0, y = 0, velocity = 0, tilt = 0, color = 0):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.tilt = tilt
        self.color = color
    def update(self):
        return
    def judge(self,cloud):
        return

# vertical ropes
class Straight_Rope(Rope):
    def update(self):
        if(self.x > 635):
            self.direction = "LEFT"
        elif(self.x < 5):
            self.direction = "RIGHT"
        if(self.direction = "RIGHT"):
            self.x += self.velocity
        elif(self.direction == "LEFT"):
            self.x -= self.velocity
        pygame.draw,line(screen, COLORS[3], [self.x, 0], [self.x, 480], 5)

    # checks if the player and the rope collided
    def judge(self, cloud):
        if(self.x > (cloud.x) and self.x < (cloud.x + 20)):
            return True
        else:
            return False
# horizontal ropes
class Straight_Rope_Horizontal(Rope):
    def update(self):
        if(self.y > 475):
            self.direction = "DOWN"
        elif(self.y < 5):
            self.direction = "UP"
        if(self.direction == "UP"):
            self.y -= self.velocity
        elif(self.direction == "DOWN"):
            self.y += self.velocity
        pygame.draw,line(screen, COLORS[3], [0, self.y], [640, self.y], 5)

    # checks if the player and the rope collided
    def judge(self, cloud):
        if(self.y > (cloud.y) and self.y < (cloud.y + 20)):
            return True
        else:
            return False

# dots(enemy)
class Shooting_Star(Rope):
    def update(self):
        self.x += self.tilt
        self.y += self.velocity
        pygame.draw.circle(screen, COLORS[self.color], [self.x self.y], 6)

    # checks if the player and the dot collided
    def judge(self, cloud):
        if((self.y > (cloud.y) and self.y < (cloud.y + 20)) and (self.x > (cloud.x) and self.x < (cloud.x + 20)))
            return True
        else:
            return False