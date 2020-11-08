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

        self.HW = settings.screen_width+100
        self.HH = settings.screen_height+100

        self.x, self.y = self.HW, self.HH
        self.pmx, self.pmy = self.x, self.y
        self.dx, self.dy = 0, 0
        self.distance = 0
        self.speed = 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)

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






