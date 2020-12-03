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
    pygame.display.set_caption("GAME")

    dan = Dan(set_settings, screen)



    enes = Group()
    oranges = Group()

    start = True

    while start:
        image = pygame.image.load('images/homescreen.bmp')
        rect = image.get_rect()
        rect.centerx = set_settings.screen_width / 2
        rect.centery = set_settings.screen_height / 2
        screen.blit(image, rect)
        pygame.display.flip()
        game_functions.check_events(set_settings, screen, dan, oranges, enes)

        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            start = False
            pygame.mixer.music.load('sounds/music.mp3')
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/music.mp3'))
            pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()

    sendin = 0
    while True:
        clock.tick(500)
        if set_settings.game_over == False:
            game_functions.game_over(enes, dan, set_settings)
            game_functions.check_events(set_settings, screen, dan, oranges, enes)
            dan.update()
            if sendin % (int(500/set_settings.enemy_difficulty)) == 0:
                game_functions.send_in_the_enemys(enes, set_settings, screen)
                if sendin % 2000 == 0:
                    set_settings.enemy_difficulty += 1
                sendin += 1
            else:
                sendin += 1

            game_functions.update_enemys(enes, dan, set_settings)
            game_functions.update_oranges(oranges, enes, set_settings)
            game_functions.screen_refresh(set_settings, screen, dan, enes, oranges)

        else:
            sendin = 0
            set_settings.enemy_difficulty = 1
            for ene in enes:
                enes.remove(ene)
            screen.fill((255, 000, 000))
            image = pygame.image.load('images/gameover.bmp')
            rect = image.get_rect()
            rect.centerx = set_settings.screen_width / 2
            rect.centery = set_settings.screen_height / 2
            screen.blit(image, rect)
            font = pygame.font.SysFont(None, 60)
            WHITE = (255, 255, 255)
            img = font.render("SCORE: " + str(set_settings.score), True, WHITE)
            screen.blit(img, (50, 50))
            pygame.display.flip()
            game_functions.check_events(set_settings, screen, dan, oranges, enes)


start_game()
