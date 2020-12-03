import pygame
from pygame.sprite import Sprite

class Dan(Sprite):

    def __init__(self, settings, screen):

        self.screen = screen
        self.settings = settings

        # Load the dan image and get its rect.
        self.image = pygame.image.load('images/dan2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = settings.screen_height/2


        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.settings.dan_speed
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.settings.dan_speed
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.settings.dan_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.settings.dan_speed

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


