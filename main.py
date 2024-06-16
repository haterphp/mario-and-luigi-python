import pygame

from game import Game
from variables import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_FPS

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    is_run = True
    clock = pygame.time.Clock()
    game_controller = Game(screen)

    while is_run:
        clock.tick(SCREEN_FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False

        game_controller.draw()
        pygame.display.update()

    game_controller.destroy()
    pygame.quit()


if __name__ == "__main__":
    main()
