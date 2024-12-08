import pygame
from main import Button, BLACK, SCREEN_RESOLUTION

def training(screen: pygame.Surface) -> int:
    """Display the main menu and handle button events.

    Args:
        screen (pygame.Surface): The surface to draw the menu on.

    Returns:
        int: The index of the selected menu option.
    """
    
    clock = pygame.time.Clock()
    pygame.display.set_caption('Meče & Duše: Trénink')
    with open('data.txt', 'r') as file:
        data = file.read().splitlines()
    button_texts = ['Melee: ' + str(data[12]), 'Block: ' + str(data[13]), 'Range: ' + str(data[14]), 'Agility: ' + str(data[15]), 'Zpět']
    screen_width, screen_height = SCREEN_RESOLUTION[0] // 2, SCREEN_RESOLUTION[1] // 2
    buttons = [
        Button(text, screen_width, screen_height + (i - (len(button_texts) // 2)) * 64)
        for i, text in enumerate(button_texts)
    ]

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return 10
            for i, button in enumerate(buttons):
                if button.handle_event(event):
                    return i + 6 if i < 4 else 0

        screen.fill(BLACK)
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()
        clock.tick(60)

