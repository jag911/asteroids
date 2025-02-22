#!/Users/thomas/bootdev/asteroids/venv/bin/python 
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroid_field import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    
    shots = pygame.sprite.Group()
    Shot.containers = (shots,updatable,drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS,shots)
    asteroid_field = AsteroidField(asteroids,updatable,drawable)

    while True:
        #catch a break!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill((0,0,0))
        drawable.draw(screen)
        
        pygame.display.flip()
        
        dt = py_clock.tick(60) / 1000

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

            if asteroid.collision(player):
                # Create font object (None uses default system font)
                font = pygame.font.Font(None, 74)  # 74 is font size
                # Render the text (text, anti-aliasing, color)
                text = font.render("Game Over", True, (255, 0, 0))  # Red text
                # Get the rectangle for positioning
                text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                # Draw to screen
                screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(1000)
                pygame.quit()
                exit()

if __name__ == "__main__":
    main()
