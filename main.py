import pygame

from game import Game
from scene import Scene
from variables import SCREEN_FPS

pygame.init()

def main():
    is_run = True
    clock = pygame.time.Clock()

    scene = Scene()
    game_controller = Game(scene)

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
