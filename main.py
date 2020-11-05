import pygame
from settings import Settings
from harvey import Harv
import game_functions

pygame.init()


def start_game():
    # Initialize game and create a screen object.
    set_settings = Settings()
    screen = pygame.display.set_mode((set_settings.screen_width, set_settings.screen_height))
    pygame.display.set_caption("Harvey Orange")

    harv = Harv(set_settings, screen)


    while True:
        game_functions.check_events(harv)
        harv.update()
        game_functions.screen_refresh(set_settings, screen, harv)



start_game()
