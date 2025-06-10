import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = Asteroid(100, 100, 20)
    asteroidfield = AsteroidField()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        dt = clock.tick(60) / 1000.0  # Convert to seconds
        screen.fill((0, 0, 0))

        # Update all sprites
        for sprite in updatable:
            sprite.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                exit()

        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
