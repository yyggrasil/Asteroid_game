import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.last_shoot = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.last_shoot > PLAYER_SHOOT_COOLDOWN:
            shot = Shot(self.position.x, self.position.y)
            forward = pygame.Vector2(0,1).rotate(self.rotation)
            shot.velocity = forward * BULLET_SPEED
            self.last_shoot = 0
            

        


    def update(self, dt):
        keys = pygame.key.get_pressed()

        # update the shoot cooldown
        self.last_shoot += dt

        # ROTATION
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # MOVEMENT
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # SHOOT
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
