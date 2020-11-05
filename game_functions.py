import sys
import pygame


def check_events(harv):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                harv.moving_right = True
            if event.key == pygame.K_LEFT:
                harv.moving_left = True
            if event.key == pygame.K_UP:
                harv.moving_up = True
            if event.key == pygame.K_DOWN:
                harv.moving_down = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                harv.moving_right = False
            if event.key == pygame.K_LEFT:
                harv.moving_left = False
            if event.key == pygame.K_UP:
                harv.moving_up = False
            if event.key == pygame.K_DOWN:
                harv.moving_down = False


def screen_refresh(settings, screen, harv):
    screen.fill(settings.background_colour)
    harv.blitme()

    pygame.display.flip()
