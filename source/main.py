import pygame
import main_menu
import level_menu

SCREEN_RESOLUTION = (1280, 960)

def init_game() -> pygame.Surface:
    """Initialize the game and return the screen surface."""
    pygame.init()
    return pygame.display.set_mode(SCREEN_RESOLUTION)

def main(scene_id: int = 0) -> None:
    """Main function of the game loop."""
    screen = init_game()

    scene_list = [
        main_menu.main_menu,
        level_menu.level_menu
    ]

    while scene_id != 9:
        scene_id = scene_list[scene_id](screen)

if __name__ == '__main__':
    main()
    pygame.quit()
    exit(0)

