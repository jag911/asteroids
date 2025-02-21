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
    player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2,radius=PLAYER_RADIUS)
    while True:
        #catch a break!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = py_clock.tick(60)

if __name__ == "__main__":
    main()
