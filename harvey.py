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

        self.rect.centerx, self.rect.centery = (0, 0)
        self.treat_x, self.treat_y = (self.settings.screen_width / 2, self.settings.screen_height / 2)

        radians = math.atan2(self.treat_y - self.rect.centery, self.treat_x - self.rect.centery)
        self.distance = math.hypot(self.treat_x - self.rect.centery, self.treat_y - self.rect.centery)
        self.distance = int(self.distance)

        self.dx = math.cos(radians)
        self.dy = math.sin(radians)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.distance >= 0:
            self.distance -= 1
            self.rect.centerx += self.dx
            self.rect.centery += self.dy





