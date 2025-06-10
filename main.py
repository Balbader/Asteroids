import pygame
from constants import *
from player import Player

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Create sprite groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

# Add player to sprite groups
player.containers = (updatable, drawable)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        dt = clock.tick(60) / 1000.0  # Convert to seconds
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        for sprite in drawable:
            sprite.draw(screen)
        for sprite in updatable:
            sprite.update(dt)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
