import pygame
from main import Button, Text, BLACK, SCREEN_RESOLUTION

def character(screen: pygame.Surface) -> int:
    """
    Display the level menu and handle user interaction.

    Args:
        screen (pygame.Surface): The surface to draw the menu on.

    Returns:
        int: The selected level number, or 9 if the window is closed.
    """
    pygame.display.set_caption('Meče & Duše: Character')
    screen_width = SCREEN_RESOLUTION[0] // 2
    screen_height = SCREEN_RESOLUTION[1] // 2 - 300
    character_texts = ['Poražený nepřítelé: ', 'Celkový dammage: ', 'Maximální úroveň: ', 'Poražení nepřátelé: ', 'Melle rekord: ', 'Block rekord: ', 'Range rekord: ', 'Agility rekord: ', 'Melle: ', 'Block: ', 'Range: ', 'Agility: ', 'Poražený nepřítel: ', 'Čas hry: ']
    buttons = [
        Button('Exit', screen_width, screen_height + 300)
    ]
    texts = [
        Text(text, screen_width, screen_height + i * 60)
        for i, text in enumerate(character_texts)
    ]

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return 10
            for button in buttons:
                if button.handle_event(event):
                    return 0

        screen.fill(BLACK)
        for button in buttons:
            button.draw(screen)
        for text in texts:
            text.draw(screen)
        pygame.display.flip()

