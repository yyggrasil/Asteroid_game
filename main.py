# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import circleshape
from constants import *
from player import Player


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # inicialize player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 20)


    while True:
        # quit when press the x on the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=BLACK)

        player.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000 # get the maximum of 60 fps and returns the delta time
        

    




if __name__ == "__main__":
    main()