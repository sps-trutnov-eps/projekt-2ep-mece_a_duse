import pygame
from main import Button, BLACK, SCREEN_RESOLUTION

def shop(screen: pygame.Surface) -> int:
    """
    Display the level menu and handle user interaction.

    Args:
        screen (pygame.Surface): The surface to draw the menu on.

    Returns:
        int: The selected level number, or 9 if the window is closed.
    """
    pygame.display.set_caption('Meče & Duše: Obchod')
    button_texts = ['Meč', 'Štít', 'Luk', 'Brnění', 'Exit']
    screen_width = SCREEN_RESOLUTION[0] // 2
    screen_height = SCREEN_RESOLUTION[1] // 2
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
                    if i == 4:
                        return 9
                    with open('data.txt', 'r') as filein, open('data.txt', 'r') as fileout:
                        data = filein.read().splitlines()
                        if data[i + 3] < 10 and (data[0] // (data[i + 3] ** data[i + 3])) >= 1:
                            data[i + 3] += 1
                        fileout.write(data)

        screen.fill(BLACK)
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

