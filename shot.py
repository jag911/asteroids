import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,SHOT_RADIUS)
        surface_size = int(self.radius * 1.5)
        self.image = pygame.Surface((surface_size,surface_size), pygame.SRCALPHA)
        pygame.draw.circle(self.image,(255,255,255),(surface_size/2,surface_size/2),self.radius,2)
        self.rect = self.image.get_rect(center=self.position)


    def update(self, dt):
        # sub-classes must override
        self.position += (self.velocity * dt)
        self.rect = self.image.get_rect(center=self.position)
        
