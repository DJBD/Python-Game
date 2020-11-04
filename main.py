import sys
import pygame
from settings import Settings
from chef import Chef

pygame.init()


def start_game():
    # Initialize game and create a screen object.
    set_settings = Settings()
    screen = pygame.display.set_mode((set_settings.screen_width, set_settings.screen_height))
    pygame.display.set_caption("Cookie Cutter")

    chef = Chef(screen)



    # Start the main loop for the game.

    while True:
        screen.fill(set_settings.background_colour)
        chef.blitme()
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


start_game()
