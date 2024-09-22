import pygame
import main_menu
import level_menu

SCREEN_RESOLUTION = (1280, 960)

class Button:
    def __init__(self, text, x, y):
        self.font = pygame.font.Font(None, 64)
        self.text = self.font.render(text, True, (255, 255, 255))
        self.rect = self.text.get_rect().center(x, y)
        self.color = None

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = (200, 200, 200) 
            else:
                self.color = (100, 100, 100)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                pass

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

