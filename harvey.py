import pygame


class Harv():

    def __init__(self, settings, screen):

        self.screen = screen
        self.settings = settings

        # Load the chef image and get its rect.
        self.image = pygame.image.load('images/harvey.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.center_x += self.settings.harvey_speed
        if self.moving_left:
            self.center_x -= self.settings.harvey_speed
        if self.moving_up:
            self.center_y -= self.settings.harvey_speed
        if self.moving_down:
            self.center_y += self.settings.harvey_speed

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
