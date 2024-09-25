import pygame
from main import Button, BLACK, SCREEN_RESOLUTION

def arena(screen: pygame.Surface) -> int:
    """
    Display the level menu and handle user interaction.

    Args:
        screen (pygame.Surface): The surface to draw the menu on.

    Returns:
        int: The selected level number, or 9 if the window is closed.
    """
    pygame.display.set_caption('Meče & Duše: Mapa Levelů')
    button_texts = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Boss']
    screen_width = SCREEN_RESOLUTION[0] // 2
    screen_height = SCREEN_RESOLUTION[1] // 2 - 150
    buttons = [
        Button(text, screen_width, screen_height + i * 60)
        for i, text in enumerate(button_texts)
    ]

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return 15
            for i, button in enumerate(buttons):
                if button.handle_event(event):
                    return i + 6

        screen.fill(BLACK)
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

