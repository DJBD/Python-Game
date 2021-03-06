import sys
import pygame

from enemy import Enemy
from oranges import Oranges
import random


def check_events(settings, screen, dan, oranges, enemys):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, dan, oranges, enemys)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, dan)


def screen_refresh(settings, screen, dan, enemys, oranges):
    screen.fill(settings.background_colour)
    font = pygame.font.SysFont(None, 60)
    RED = (255, 0, 0)
    img = font.render("SCORE: " + str(settings.score), True, RED)
    screen.blit(img, (50, 50))

    for orange in oranges.sprites():
        orange.draw_orange()

    for enemy in enemys.sprites():
        enemy.draw_enemy()

    dan.blitme()
    pygame.display.flip()


def check_keydown_events(event, settings, screen, dan, oranges, enemys):
    if event.key == pygame.K_RIGHT:
        dan.moving_right = True
    if event.key == pygame.K_LEFT:
        dan.moving_left = True
    if event.key == pygame.K_UP:
        dan.moving_up = True
    if event.key == pygame.K_DOWN:
        dan.moving_down = True

    if event.key == pygame.K_w:
        # Create a new orange and add it to the orange group.
        new_orange = Oranges(settings, screen, dan)
        new_orange.direction = "UP"
        oranges.add(new_orange)

    if event.key == pygame.K_s:
        # Create a new orange and add it to the orange group.
        new_orange = Oranges(settings, screen, dan)
        new_orange.direction = "DOWN"
        oranges.add(new_orange)

    if event.key == pygame.K_a:
        # Create a new orange and add it to the orange group.
        new_orange = Oranges(settings, screen, dan)
        new_orange.direction = "LEFT"
        oranges.add(new_orange)

    if event.key == pygame.K_d:
        # Create a new orange and add it to the orange group.
        new_orange = Oranges(settings, screen, dan)
        new_orange.direction = "RIGHT"
        oranges.add(new_orange)

    if event.key == pygame.K_RETURN:
        settings.game_over = False
        settings.score = 0


def check_keyup_events(event, dan):
    if event.key == pygame.K_RIGHT:
        dan.moving_right = False
    if event.key == pygame.K_LEFT:
        dan.moving_left = False
    if event.key == pygame.K_UP:
        dan.moving_up = False
    if event.key == pygame.K_DOWN:
        dan.moving_down = False


def update_oranges(oranges, enemys, settings):
    # Update orange positions.
    oranges.update()
    if (pygame.sprite.groupcollide(oranges, enemys, True, True)):
        enemy_scream(settings)
        settings.score += 1
    # Get rid of oranges that have disappeared.
    for o in oranges.copy():
        if o.rect.y <= 0 or o.rect.x <= 0 or o.rect.y >= settings.screen_height or o.rect.x >= settings.screen_width:
            oranges.remove(o)


def update_enemys(enemy, Dan, settings):
    # update enemy positions.
    enemy.update(Dan)


def game_over(enemys, Dan, settings):
    for enemy in enemys:
        if (pygame.sprite.collide_rect(Dan, enemy)):
            settings.game_over = True


def send_in_the_enemys(enemys, settings, screen):
    new_harv = Enemy(settings, screen)
    enemys.add(new_harv)


def enemy_scream(settings):
    scream = {

        # HARVEY NOISE
        1: {
        # enemy
        1: pygame.mixer.Sound('sounds/gee.mp3'),
        2: pygame.mixer.Sound('sounds/bolognesey.mp3'),
        3: pygame.mixer.Sound('sounds/gurluckla.mp3'),
        4: pygame.mixer.Sound('sounds/mcgoo.mp3'),
        5: pygame.mixer.Sound('sounds/ooo.mp3'),
        6: pygame.mixer.Sound('sounds/solonely.mp3'),
        7: pygame.mixer.Sound('sounds/urghh.mp3')
        },

        # WILL NOISE
        2:{

        1: pygame.mixer.Sound('sounds/willwhat.mp3'),
        2: pygame.mixer.Sound('sounds/willbecky.mp3'),
        3: pygame.mixer.Sound('sounds/willspurs.mp3'),
        4: pygame.mixer.Sound('sounds/thatsfacts.mp3'),
        5: pygame.mixer.Sound('sounds/fire.mp3'),
        6: pygame.mixer.Sound('sounds/yournotwill.mp3'),
        7: pygame.mixer.Sound('sounds/notabite.mp3')
        }
    }
    rand = random.randint(1, 7)
    pygame.mixer.Channel(rand).play(scream[settings.enemy].get(rand))
