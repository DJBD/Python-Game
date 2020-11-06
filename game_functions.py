import sys
import pygame

import settings
from oranges import Oranges


def check_events(settings, screen, dan, oranges):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, dan, oranges)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, dan)


def screen_refresh(settings, screen, dan, oranges):
    screen.fill(settings.background_colour)

    for orange in oranges.sprites():
        orange.draw_orange()

    dan.blitme()

    pygame.display.flip()


def check_keydown_events(event, settings, screen, dan, oranges):
    if event.key == pygame.K_RIGHT:
        dan.moving_right = True
    if event.key == pygame.K_LEFT:
        dan.moving_left = True
    if event.key == pygame.K_UP:
        dan.moving_up = True
    if event.key == pygame.K_DOWN:
        dan.moving_down = True

    elif event.key == pygame.K_w:
        # Create a new bullet and add it to the bullets group.
        new_orange = Oranges(settings, screen, dan)
        new_orange.direction = "UP"
        oranges.add(new_orange)

    elif event.key == pygame.K_s:
        # Create a new bullet and add it to the bullets group.
        new_orange = Oranges(settings, screen, dan)
        new_orange.direction = "DOWN"
        oranges.add(new_orange)

    elif event.key == pygame.K_a:
        # Create a new bullet and add it to the bullets group.
        new_orange = Oranges(settings, screen, dan)
        new_orange.direction = "LEFT"
        oranges.add(new_orange)

    elif event.key == pygame.K_d:
        # Create a new bullet and add it to the bullets group.
        new_orange = Oranges(settings, screen, dan)
        new_orange.direction = "RIGHT"
        oranges.add(new_orange)


def check_keyup_events(event, dan):
    if event.key == pygame.K_RIGHT:
        dan.moving_right = False
    if event.key == pygame.K_LEFT:
        dan.moving_left = False
    if event.key == pygame.K_UP:
        dan.moving_up = False
    if event.key == pygame.K_DOWN:
        dan.moving_down = False


def update_oranges(oranges, settings):
    # Update bullet positions.
    oranges.update()
    # Get rid of bullets that have disappeared.
    for o in oranges.copy():
        if o.rect.y <= 0 or o.rect.x <= 0 or o.rect.y >= settings.screen_height or o.rect.x >= settings.screen_width:
            oranges.remove(o)
