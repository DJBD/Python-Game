import sys
import pygame

pygame.init()


def start_game():
    # Initialize game and create a screen object.
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Cookie Cutter")

    # Start the main loop for the game.

    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


start_game()
