import pygame

def main_menu(screen: pygame.Surface) -> int:
    pygame.display.set_caption('Meče & Duše')

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit(0)

        screen.fill(BLACK)
        button_1 = Button('Postava', screen, SCREEN_RESOLUTION(0) // 2, SCREEN_RESOLUTION(1) // 2)
        button_2 = Button('Aréna', screen, SCREEN_RESOLUTION(0) // 2, SCREEN_RESOLUTION(1) // 2)
        button_3 = Button('Trénink', screen, SCREEN_RESOLUTION(0) // 2, SCREEN_RESOLUTION(1) // 2)
        button_4 = Button('Obchod', screen, SCREEN_RESOLUTION(0) // 2, SCREEN_RESOLUTION(1) // 2)
        button_5 = Button('Muzeum', screen, SCREEN_RESOLUTION(0) // 2, SCREEN_RESOLUTION(1) // 2)

