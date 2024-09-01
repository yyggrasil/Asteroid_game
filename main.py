import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateble = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # inicialize player
    Player.containers = (updateble, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 20)

    # inicialize asteroid
    Asteroid.containers = (updateble, drawable, asteroids)

    # incialize asteroid field
    AsteroidField.containers = (updateble)
    asteroid_field = AsteroidField()

    while True:
        # quit when press the x on the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=BLACK)

        for object in updateble:
            object.update(dt)
        
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000 # get the maximum of 60 fps and returns the delta time
        

if __name__ == "__main__":
    main()