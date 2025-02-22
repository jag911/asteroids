from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius, shots, timer = 0):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots
        self.cooldown = timer
        # Create a transparent surface
        surface_size = int(radius * 2.5)
        self.image = pygame.Surface((surface_size,surface_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        # Update rect position
        self.rect.center = self.position
        
        # Clear previous drawing
        self.image.fill((0,0,0,0))
        
        # Convert triangle points to local coordinates
        local_points = [point - self.position + pygame.Vector2(self.image.get_width()/2, self.image.get_height()/2) 
                    for point in self.triangle()]
        
        # Draw triangle on image surface
        pygame.draw.polygon(self.image, (255,255,255), local_points, 2)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self,dt):
        if self.cooldown <= 0:
            self.cooldown = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x,self.position.y)
            velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = velocity * PLAYER_SHOOT_SPEED
            self.shots.add(shot)
        self.cooldown -= dt
