import pygame
from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.angle = 0  # Initialize angle to 0 (pointing upward)

    def rotate(self, dt):
        self.angle += PLAYER_TURN_SPEED * dt

    def move(self, dt, direction):
        # Create a vector pointing in the direction the player is facing
        forward = pygame.Vector2(0, -1).rotate(self.angle)
        # Scale it by the movement speed and direction
        self.velocity = forward * PLAYER_MOVE_SPEED * direction

    def keep_in_bounds(self):
        # Keep the center position within bounds
        self.position.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.position.x))
        self.position.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.position.y))

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Rotation controls
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Movement controls
        if keys[pygame.K_w]:
            self.move(dt, 1)  # Move forward
        elif keys[pygame.K_s]:
            self.move(dt, -1)  # Move backward
        else:
            self.velocity = pygame.Vector2(0, 0)

        # Update position based on velocity
        self.position += self.velocity * dt

        # Keep the player within screen bounds
        self.keep_in_bounds()

    def draw(self, screen):
        # Draw the player as a triangle
        forward = pygame.Vector2(0, -1).rotate(self.angle)
        right = pygame.Vector2(1, 0).rotate(self.angle)

        # Calculate triangle points
        tip = self.position + forward * self.radius
        left = self.position - forward * self.radius/2 + right * self.radius/2
        right = self.position - forward * self.radius/2 - right * self.radius/2

        pygame.draw.polygon(screen, (255, 255, 255), [tip, left, right])
