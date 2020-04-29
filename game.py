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

def open():
    endFlag = False
    font1 = pygame.font.SysFont(None, 80)
    text1 = font1.render("Cloud Jump the Rope", False, (255, 255, 255))
    font2 = pygame.font.SysFont(None, 80)
    text2 = font1.rendet("Press Any Key for Start", False, (255, 255, 255))

    while endFlag == False:
        screen.fill((0, 0, 0))
        screen.blit(text1, (30, 50))
        screen.blit(text2, (20, 150))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endFlag = True
            elif event.type == pygame.KEYDOWN:
                endFlag = True
                main()

def main():
    endFlag = Cloud(400, 400)
    time_elapsed = 0
    force_quit = False

    ropes = []

    while endFlag == False:
        clock.tick(60)
        time_elapsed += 1
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endFlag = True
                force_quit = True
            else:
                cloud.update(event)

        # move the player
        if cloud.move_right == True:
            if cloud.x < 620:
                cloud.x += CLOUD_VELOCITY
        if cloud.move_left == True:
            if cloud.x > 00:
                cloud.x -= CLOUD_VELOCITY
        if cloud.move_up == True:
            if cloud.y > 00:
                cloud.y -= CLOUD_VELOCITY
        if cloud.move_down == True:
            if cloud.y < 460:
                cloud.y += CLOUD_VELOCITY

        if (time_elapsed == 20):
            straight_rope = Straight_Rope(0, 0, 3)
            ropes.append(straight_rope)
        if (time_elapsed == 300):
            straight_rope_horizontal = Straight_Rope_Horizontal(0, 0, 3)
            ropes.append(straight_rope_horizontal)
        if (time_elapsed == 600):
            straight_rope = Straight_Rope(0, 0, 3)
            ropes.append(straight_rope)
        if (time_elapsed == 860):
            straight_rope_horizontal =Straight_Rope_Horizontal](0, 0, 3)
            ropes.append(straight_rope_horizontal)
        if(random.randrange(200) < 6):
            shooting_star1 = Shooting_Star(random.randrange(640), 0, random.randrange(5) + 5, random.randrange(10) - 5)
            ropes.append(shooting_star1)
            shooting_star2 = Shooting_Star(random.randrange(640), 0, random.randrange(5) + 5, random.randrange(10) - 5)
            ropes.append(shooting_star2)
            shooting_star3 = Shooting_Star(10, random.randrange(480), 0, random.randrange(5) + 5, random.randrange(10) - 5)
            ropes.append(shooting_star3)
            shooting_star4 = Shooting_Star(10, random.randrange(480), 0, random.randrange(5) + 5, random.randrange(10) - 5)
            ropes.append(shooting_star4)

        # move all the topers and dots
        for roper in ropes:
            rope.update()
            if (rope.x < 0 or rope.x > 640) or (rope.y < 0 or rope.y > 480):
                ropes.remove(rope)
            if(time_elapsed % 1000 == 0) and time_elapsed != 0:
                rope.velocity += 1

        # if the plalyer is jumping, don't check if it collided with rope or dots
        if(cloud.immunity == True):
            cloud.immunity_count += 1
            if (cloud.immunity_count < CLOUD_JUMP) :
                screen.blit(cloud.immune_image, (cloud.x, cloud.y))
            else:
                cloud.immunity = False
                cloud.immunity_count = 0
                screen.blit(cloud.image, (cloud.x, cloud.y))
        else:
            screen.blit(cloud.image, (cloud,x, cloud.y))
            for rope in ropes:
                if(rope.judge(cloud) == True) and (cloud.life_lost_time + 30 < time_elapsed):
                    cloud.life_lost_time = time_elapsed
                    cloud.life -= 1
                    if cloud.life == 0:
                        endFlag = True
        for i in range(cloud.life -1):
            screen.blit(heart_image, (i * 30, 50))
        pygame.display.update()
    quit(time_elapsed, force_quit)
                