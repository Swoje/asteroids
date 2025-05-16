# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys
from shot import Shot


def main ():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    running = True  #not present in solution files
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)  

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisionCheck(shot) == True:
                    asteroid.split()
                    shot.kill()

        for asteroid in asteroids:
            if asteroid.collisionCheck(player) == True:
                print("Game over!")
                sys.exit()
        screen.fill((0,0,0))
        #screen.fill("black")  from solution files
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()