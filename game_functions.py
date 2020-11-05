import sys
import pygame

def check_events():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def screen_refresh(settings, screen, harv):
    screen.fill(settings.background_colour)
    harv.blitme()

    pygame.display.flip()
