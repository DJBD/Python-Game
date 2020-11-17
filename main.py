import pygame
from settings import Settings
from dan import Dan
from harvey import Harvey
import game_functions
from pygame.sprite import Group
import time

pygame.init()


def start_game():
    # Initialize game and create a screen object.
    set_settings = Settings()
    screen = pygame.display.set_mode((set_settings.screen_width, set_settings.screen_height))
    pygame.display.set_caption("Harvey Eats Oranges")

    dan = Dan(set_settings, screen)

    harvs = Group()
    oranges = Group()

    start = True

    while start:
        image = pygame.image.load('images/homescreen.bmp')
        rect = image.get_rect()
        rect.centerx = set_settings.screen_width / 2
        rect.centery = set_settings.screen_height / 2
        screen.blit(image, rect)
        pygame.display.flip()
        game_functions.check_events(set_settings, screen, dan, oranges, harvs)

        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            start = False

    clock = pygame.time.Clock()

    sendin = 0

    while True:
        clock.tick(500)

        if set_settings.game_over == False:
            game_functions.game_over(harvs, dan, set_settings)
            game_functions.check_events(set_settings, screen, dan, oranges, harvs)
            dan.update()
            if sendin % (int(500/set_settings.harvey_difficulty)) == 0:
                game_functions.send_in_the_harveys(harvs, set_settings, screen)
                if sendin % 2000 == 0:
                    set_settings.harvey_difficulty += 1
                sendin += 1
            else:
                sendin += 1

            game_functions.update_harveys(harvs, dan, set_settings)
            game_functions.update_oranges(oranges, harvs, set_settings)
            game_functions.screen_refresh(set_settings, screen, dan, harvs, oranges)

        else:
            sendin = 0
            set_settings.harvey_difficulty = 1
            for harv in harvs:
                harvs.remove(harv)
            screen.fill((255, 000, 000))
            image = pygame.image.load('images/gameover.bmp')
            rect = image.get_rect()
            rect.centerx = set_settings.screen_width / 2
            rect.centery = set_settings.screen_height / 2
            screen.blit(image, rect)
            pygame.display.flip()
            game_functions.check_events(set_settings, screen, dan, oranges, harvs)


start_game()
