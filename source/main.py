import pygame

SCREEN_RESOLUTION = (1080, 720)
WHITE = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)
GREY = (100, 100, 100)
BLACK = (50, 50, 50)

class Button:
    """A class to represent a button in the game."""

    def __init__(self, text: str, x: int, y: int) -> None:
        """Initialize the button with text, position, and default color."""
        self.font = pygame.font.Font(None, 64)
        self.text = self.font.render(text, True, WHITE)
        self.rect = self.text.get_rect(center=(x, y))
        self.color = GREY

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the button on the screen."""
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, self.rect)

    def handle_event(self, event: pygame.event.Event) -> bool:
        """Handle mouse events for the button.

        Args:
            event (pygame.event.Event): The event to handle.

        Returns:
            bool: True if the button is clicked, False otherwise.
        """
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = LIGHT_GREY
            else:
                self.color = GREY
        elif event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True
        return False

class Text:
    """A class to represent a text in the game."""

    def __init__(self, text: str, x: int, y: int) -> None:
        """Initialize the text, position, and default color."""
        self.font = pygame.font.Font(None, 64)
        self.text = self.font.render(text, True, WHITE)
        self.rect = self.text.get_rect(center=(x, y))

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the text on the screen."""
        screen.blit(self.text, self.rect)

def main(scene_id: int = 0) -> None:
    """Main function of the game loop.

    Args:
        scene_id (int): The initial scene ID. Defaults to 0.
    """
    from menu import menu
    from arena import arena
    from shop import shop
    from training import training
    from museum import museum
    from melee import melee
    from block import block
    from range import range
    from agility import agility
    from postava import postava

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_RESOLUTION)

    scene_list = [
        menu,
        postava,
        arena,
        training,
        shop,
        museum,
        melee,
        block,
        range,
        agility
    ]

    while scene_id != 10:
        scene_id = scene_list[scene_id](screen)
    pygame.quit()

if __name__ == '__main__':
    main()
    exit(0)
