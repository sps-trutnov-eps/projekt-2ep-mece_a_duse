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
    with open('data.txt', 'r') as file:
        data = file.read().splitlines()
        data = [int(item) for item in data]
    
    coin = pygame.image.load("sprites/coin.png")
    screen_width = SCREEN_RESOLUTION[0] // 2
    screen_height = SCREEN_RESOLUTION[1] // 2
    
    font=pygame.font.Font(None, 40)
    a=0
    b=0
    c=0
    while True:
	button_texts = ['Meč ' + str(data[3]), 'Štít ' + str(data[5]), 'Luk ' + str(data[6]), 'Brnění ' + str(data[4]), 'Back']
	buttons = [
        	Button(text, screen_width, screen_height + (i - (len(button_texts) // 2)) * 64)
        	for i, text in enumerate(button_texts)
    	]
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return 10
            for i, button in enumerate(buttons):
                if button.handle_event(event):
                    if i == 4:
                        return 0
                    if data[i + 3] < 10 and 20**data[i+3] <= data[0]:
                        data[0]-=20**data[i+3]
                        data[i + 3] += 1
                    data[0]=int(data[0])
                    with open("data.txt", "w") as file:
                        file.writelines([str(item)+"\n" for item in data])

        screen.fill(BLACK)
        for button in buttons:
            button.draw(screen)
        a=data[0]
        if a>1000:
            b=0
            while a>10:
                a/=10
                a=round(a,3)
                b+=1
            text=font.render(str(a)+"E"+str(b), True, (255,255,255))
        else:
            text=font.render(str(a), True, (255,255,255))
        screen.blit(text,(SCREEN_RESOLUTION[0]-150,SCREEN_RESOLUTION[1]-40))
        screen.blit(coin,(SCREEN_RESOLUTION[0]-50,SCREEN_RESOLUTION[1]-50))
        b=0
        a=0
        c=0
        while b<4:
            a=20**(int(data[b+3]))
            c=0
            if a>1000:
                while a>10:
                    a=round(a/10,3)
                    c+=1
                text=font.render(str(a)+"E"+str(c), True, (255,255,255))
            else:
                text=font.render(str(a), True, (255,255,255))
            screen.blit(text,(SCREEN_RESOLUTION[0]/2+100,220+b*65))
            b+=1
        
        
        
        
        
        pygame.display.flip()
        clock.tick(60)
