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
    clock = pygame.time.Clock()
    pygame.display.set_caption('Meče & Duše: Obchod')
    button_texts = ['Meč', 'Štít', 'Luk', 'Brnění', 'Exit']
    coin=pygame.image.load("sprites/coin.png")
    screen_width = SCREEN_RESOLUTION[0] // 2
    screen_height = SCREEN_RESOLUTION[1] // 2
    buttons = [
        Button(text, screen_width, screen_height + (i - (len(button_texts) // 2)) * 64)
        for i, text in enumerate(button_texts)
    ]
    font=pygame.font.Font(None, 40)
    a=0
    b=0
    with open('data.txt', 'r') as filein, open('data.txt', 'r') as fileout:
        data = filein.read().splitlines()
        data = [int(item) for item in data]
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return 10
            for i, button in enumerate(buttons):
                if button.handle_event(event):
                    if i == 4:
                        return 0
                    if data[i + 3] < 10 and 1.5*10**data[i+3] <= data[0]:
                        data[0]-=1.5*10**data[i+3]
                        data[i + 3] += 1
                    data[0]=int(data[0])
                    with open("data.txt", "w") as file:
                        file.writelines([str(item)+"\n" for item in data])

        screen.fill(BLACK)
        for button in buttons:
            button.draw(screen)
        a=data[0]
        b=0
        while a>10:
            a/=10
            a=round(a,3)
            b+=1
        text=font.render(str(a)+"E"+str(b), True, (255,255,255))
        screen.blit(text,(SCREEN_RESOLUTION[0]-150,SCREEN_RESOLUTION[1]-40))
        screen.blit(coin,(SCREEN_RESOLUTION[0]-50,SCREEN_RESOLUTION[1]-50))
        b=0
        while b<4:
            text=font.render("1.5E"+str(data[3+b]), True, (255,255,255))
            screen.blit(text,(SCREEN_RESOLUTION[0]/2+80,220+b*65))
            b+=1
        
        
        
        
        
        pygame.display.flip()
        clock.tick(60)

