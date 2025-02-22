import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius,group_asteroid,group_update,group_draw):
        super().__init__(x,y,radius)
        self.__group_asteroids = group_asteroid
        self.__group_updatable = group_update
        self.__group_drawable = group_draw
        self.containers = (group_asteroid,group_update,group_draw)
        surface_size = int(self.radius * 2)
        self.image = pygame.Surface((surface_size,surface_size), pygame.SRCALPHA)
        pygame.draw.circle(self.image,(255,255,255),(surface_size/2,surface_size/2),self.radius,2)
        self.rect = self.image.get_rect(center=self.position)


    def update(self, dt):
        # sub-classes must override
        self.position += (self.velocity * dt)
        self.rect = self.image.get_rect(center=self.position)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        angle = random.uniform(20,50)
        asteroid_1 = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS,self.__group_asteroids,self.__group_updatable,self.__group_drawable)
        asteroid_1.velocity = self.velocity.copy().rotate(angle)
        asteroid_1.velocity *= 1.2
        asteroid_2 = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS,self.__group_asteroids,self.__group_updatable,self.__group_drawable)
        asteroid_2.velocity = self.velocity.copy().rotate(-angle)
        asteroid_2.velocity *= 1.2
