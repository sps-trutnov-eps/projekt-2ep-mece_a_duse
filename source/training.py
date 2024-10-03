import pygame
from main import Button, BLACK, SCREEN_RESOLUTION

def training(screen: pygame.Surface) -> int:
    """Display the main menu and handle button events.

    Args:
        screen (pygame.Surface): The surface to draw the menu on.

    Returns:
        int: The index of the selected menu option.
    """
    pygame.display.set_caption('Meče & Duše')
    button_texts = ['Melee', 'Block', 'Range', 'Agility']
    screen_width = SCREEN_RESOLUTION[0] // 2
    screen_height = SCREEN_RESOLUTION[1] // 2 - (64 * (len(button_texts // 2)))
    buttons = [
        Button(text, screen_width, screen_height + i * 64)
        for i, text in enumerate(button_texts)
    ]

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return 10
            for i, button in enumerate(buttons):
                if button.handle_event(event):
                    return i + 6

        screen.fill(BLACK)
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

