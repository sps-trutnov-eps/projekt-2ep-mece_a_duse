import pygame

def draw_text(text, surface, x, y):
    font = pygame.font.Font(None, 74)
    textobj = font.render(text, True, (255, 255, 255))
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main_menu(screen: pygame.Surface) -> int:
    pygame.display.set_caption('Meče & Duše')

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit(0)

        screen.fill(BLACK)

