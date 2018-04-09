import pygame
from random import *

pad_width = 1024
pad_height = 768
BgColor = (255, 255, 255)

pygame.init()
game_pad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("My PyGame")

# prepare resources
bgImage = pygame.image.load("bg1.png").convert()
bgImage = pygame.transform.scale(bgimage, (pad_width, pad_height))

clock = pygame.time.Clock()

quit = False
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    # draw background
    game_pad.fill(BgColor)
    game_pad.blit(bgImage, (0,0))

    # update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
