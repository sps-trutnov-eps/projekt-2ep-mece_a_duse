import pygame
from main import Button, Text, BLACK, SCREEN_RESOLUTION

def postava(screen: pygame.Surface) -> int:
    """
    Display the level menu and handle user interaction.

    Args:
        screen (pygame.Surface): The surface to draw the menu on.

    Returns:
        int: The 0 to return to the main menu, or 9 if the window is closed.
    """
    pygame.display.set_caption('Meče & Duše: Character')
    clock = pygame.time.Clock()
    with open('data.txt', 'r') as file:
        data = file.read().splitlines()
    character_texts = ['peníze: : ' + data[0],"životy: "+data[12],'demage: ' + data[11], 'štít: ' + data[13], 'luk: ' + data[14], 'agility: ' + data[15], 'potion 1: ' + data[7], 'potion 2: ' + data[8]]
    character_texts2= ['level: ' + data[1],"xp: "+str(round(int(data[2])/(100+1.5**int(data[1])/2)*100,1))+"%",'výzboroj brnění: ' + data[4], 'výzboroj meč: ' + data[3], 'výzboroj štít: ' + data[5], 'výzboroj luk: ' + data[6], 'potion 3: ' + data[9], 'potion 4: ' + data[9]]
    screen_height = SCREEN_RESOLUTION[1] // 2
    buttons = [
        Button('Exit', SCREEN_RESOLUTION[0]//2, screen_height + (64 * ((len(character_texts) // 2) + 1)))
    ]
    texts = [
        Text(text, SCREEN_RESOLUTION[0]//3-50, screen_height - (64 * ((len(character_texts) // 2) - i)))
        for i, text in enumerate(character_texts)
    ]
    texts2 = [
        Text(text2, SCREEN_RESOLUTION[0]*2//3+50, screen_height - (64 * ((len(character_texts2) // 2) - j)))
        for j, text2 in enumerate(character_texts2)
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
        for text2 in texts2:
            text2.draw(screen)
        pygame.display.flip()
        clock.tick(60)
