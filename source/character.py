import pygame
from main import Button, Text, BLACK, SCREEN_RESOLUTION

def character(screen: pygame.Surface) -> int:
    """
    Display the level menu and handle user interaction.

    Args:
        screen (pygame.Surface): The surface to draw the menu on.

    Returns:
        int: The 0 to return to the main menu, or 9 if the window is closed.
    """
    pygame.display.set_caption('Meče & Duše: Character')
    with open('data.txt', 'r') as file:
        data = file.read().splitlines()
    character_texts = ['Melle: ' + str(data[]), 'Block: ' + str(data[13]), 'Range: ' + str(data[14]), 'Agility: ' + str(data[15])]
    screen_width = SCREEN_RESOLUTION[0] // 2
    buttons = [
        Button('Exit', screen_width, (64 * len(character_texts)))
    ]
    texts = [
        Text(text, screen_width, (64 * i))
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

