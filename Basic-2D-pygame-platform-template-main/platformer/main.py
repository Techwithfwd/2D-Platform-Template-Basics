import pygame, sys
from settings import *
from level import Level
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Platform Template')
clock = pygame.time.Clock()
# Importing my level.py which contains my game set up
level = Level(level_map,screen)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('black')
    level.run()
    # test_tile.draw(screen)

    pygame.display.update()
    clock.tick(60) 