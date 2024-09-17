import pygame
import main_menu
import level_menu

SCREEN_RESOLUTION = (1280, 960)

def init_game() -> pygame.Surface:
    """Initialization of the game and return of the screen surface."""
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_RESOLUTION)
    return screen

def main(scene_id: int = 0) -> None:
    """Main function of the game loop."""
    screen = init_game()

    loop_list = [
        main_menu.main_menu,
        level_menu.level_menu
    ]

    while True:
        scene_id = loop_list[scene_id](screen)

if __name__ == '__main__':
    main()
    pygame.quit()
    exit(0)
