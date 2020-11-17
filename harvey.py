import random
import sys

import pygame
import math
from pygame.sprite import Sprite


class Harvey(Sprite):
    def __init__(self, settings, screen):
        super(Harvey, self).__init__()

        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/harvey.bmp')
        self.rect = self.image.get_rect()
        #self.rect.inflate_ip(-20, -20)

        plus_x_range, y_range = random.randint(0, 1920), random.choice([1200, -500])
        x_range, pos_y_range = random.choice([-200,2000]), random.randint(0,1080)

        self.HW, self.HH = random.choice([(plus_x_range, y_range), (x_range, pos_y_range)])

        self.x, self.y = self.HW, self.HH
        self.pmx, self.pmy = self.x, self.y
        self.dx, self.dy = 0, 0
        self.distance = 0
        self.speed = settings.harvey_speed

    def draw_harvey(self):
        self.screen.blit(self.image, self.rect )

    def update(self, dan):
        if not self.distance:
            mx, my = dan.rect.centerx, dan.rect.centery

            radians = math.atan2(my - self.pmy, mx - self.pmx)
            self.distance = math.hypot(mx - self.pmx, my - self.pmy) / self.speed
            self.distance = int(self.distance)

            self.dx = math.cos(radians) * self.speed
            self.dy = math.sin(radians) * self.speed

            self.pmx, self.pmy = mx, my

        if self.distance:
            self.distance -= 1
            self.x += self.dx
            self.y += self.dy

        self.rect.centerx = self.x
        self.rect.centery = self.y










