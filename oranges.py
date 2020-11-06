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
        self.x = float(self.rect.x)

        self.speed = settings.orange_speed
        self.direction = ""

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        if self.direction == "UP": self.update_move_up()
        if self.direction == "DOWN": self.update_move_down()
        if self.direction == "LEFT": self.update_move_left()
        if self.direction == "RIGHT": self.update_move_right()

    def draw_orange(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)

    def update_move_up(self):
        self.y -= self.speed
        # Update the rect position.
        self.rect.y = self.y

    def update_move_down(self):
        self.y += self.speed
        # Update the rect position.
        self.rect.y = self.y

    def update_move_left(self):
        self.x -= self.speed
        # Update the rect position.
        self.rect.x = self.x

    def update_move_right(self):
        self.x += self.speed
        # Update the rect position.
        self.rect.x = self.x



