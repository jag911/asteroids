#!/Users/thomas/bootdev/asteroids/venv/bin/python 
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    while True:
        #catch a break!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)

        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        
        dt = py_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
