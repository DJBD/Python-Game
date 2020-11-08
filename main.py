import pygame
from settings import Settings
from dan import Dan
from harvey import Harvey
import game_functions
from pygame.sprite import Group

pygame.init()


def start_game():
    # Initialize game and create a screen object.
    set_settings = Settings()
    screen = pygame.display.set_mode((set_settings.screen_width, set_settings.screen_height))
    pygame.display.set_caption("Harvey Eats Oranges")

    dan = Dan(set_settings, screen)
    harv = Harvey(set_settings, screen)

    harvs = Group()
    oranges = Group()




    while True:
        game_functions.check_events(set_settings, screen, dan, oranges, harvs)
        dan.update()
        harv.update(dan)
        game_functions.update_harveys(harvs, dan, set_settings)
        game_functions.update_oranges(oranges, set_settings)
        game_functions.screen_refresh(set_settings, screen, dan, harvs, oranges)



start_game()
