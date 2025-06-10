import pygame
from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.angle = 0  # Initialize angle to 0 (pointing upward)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.angle)
        right = (
            pygame.Vector2(0, 1).rotate(self.angle + 90) * self.radius / 1.5
        )
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        return super().draw(screen)
