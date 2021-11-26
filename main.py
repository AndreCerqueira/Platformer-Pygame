import pygame
import os
from settings import *
from level import Level

pygame.font.init()
pygame.mixer.init()

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game!")
clock = pygame.time.Clock()
level = Level(level_map, WIN)

# https://www.youtube.com/watch?v=YWN8GcmJ-jA&t=344s
# 51:00 min

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
        WIN.fill('black')
        level.run()

        pygame.display.update()
        clock.tick(FPS)

    main()



if __name__ == "__main__":
    main()