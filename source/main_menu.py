import pygame
from main import Button, SCREEN_RESOLUTION

def main_menu(screen: pygame.Surface) -> int:
    pygame.display.set_caption('Meče & Duše')

    button_texts = ['Postava', 'Aréna', 'Trénink', 'Obchod', 'Muzeum']
    buttons = [Button(text, SCREEN_RESOLUTION(0) // 2, SCREEN_RESOLUTION(1) // 2 + i * 60 - 150) for i, text in enumerate(button_texts)]

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return 9
            for button in buttons:
                button.handle_event(event)

        screen.fill(BLACK)
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

