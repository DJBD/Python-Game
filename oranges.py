import pygame
from pygame.sprite import Sprite


class Oranges(Sprite):

    def __init__(self, settings, screen, dan):
        """Create an orange object at the ship's current position."""

        # Load the orange image and get its rect.
        self.image = pygame.image.load('images/orange.bmp')
        self.rect = self.image.get_rect()

        super(Oranges, self).__init__()
        self.screen = screen

        self.rect.centerx = dan.rect.centerx
        self.rect.top = dan.rect.top

        self.y = float(self.rect.y)

        self.speed = settings.orange_speed

        self.shooting_up = False
        self.shooting_down = False
        self.shooting_left = False
        self.shooting_right = False

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        if self.shooting_up:
            self.y -= self.speed
            # Update the rect position.
            self.rect.y = self.y

        if self.shooting_down:
            self.y += self.speed
            # Update the rect position.
            self.rect.y = self.y

    def draw_orange(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)



