import pygame
from settings import Settings
from dan import Dan
import game_functions
from pygame.sprite import Group

pygame.init()


def start_game():
    # Initialize game and create a screen object.
    set_settings = Settings()
    screen = pygame.display.set_mode((set_settings.screen_width, set_settings.screen_height))
    pygame.display.set_caption("Harvey Eats Orwanges")

    dan = Dan(set_settings, screen)

    oranges = Group()


    while True:
        game_functions.check_events(set_settings, screen, dan, oranges)
        dan.update()
        game_functions.update_oranges(oranges, set_settings)
        game_functions.screen_refresh(set_settings, screen, dan, oranges)



start_game()
