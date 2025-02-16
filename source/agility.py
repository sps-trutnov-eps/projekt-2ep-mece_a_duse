import pygame
import random
from main import WHITE, SCREEN_RESOLUTION

def agility(screen: pygame.Surface) -> int:
    """
    XXX

    Returns:
        int: score if the player collides with an apple.
    """
    # Screen dimensions
    screen_width, screen_height = SCREEN_RESOLUTION

    # Load images
    player_image = pygame.image.load('sprites/hrac sam.png')
    apple_image = pygame.image.load('sprites/apple.png')
    pozadi=pygame.image.load("sprites/pozadi.png")
    font=pygame.font.Font(None, 64) 

    # Scale images
    player_image = pygame.transform.scale(player_image, (128, 128))
    apple_image = pygame.transform.scale(apple_image, (64, 64))

    # Player settings
    player_width = player_image.get_width()
    player_height = player_image.get_height()
    player_x = (screen_width - player_width) // 2
    player_y = screen_height - player_height

    # Apple settings
    apple_width = apple_image.get_width()
    apple_height = apple_image.get_height()
    apple_speed = 6
    apple_frequency = 180

    # Initialize player and apple positions
    player = pygame.Rect(player_x, player_y, player_width, player_height)
    apples_x = []
    apples_y = []
    apples__x = []
    a=0
    b=0
    flip=False 
    with open("data.txt", "r") as file:
        input = [int(line.strip()) for line in file]
    
    # Game loop control
    clock = pygame.time.Clock()
    score = 0
    frame_count = 0
    
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 10
        b=2
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.x = player_x
            player.y = player_y - player_height
            b=a
            a=0
        if keys[pygame.K_DOWN]:
            player.x = player_x
            player.y = player_y
            b=a
            a=0
        if keys[pygame.K_LEFT]:
            player.x = player_x - player_width
            player.y = player_y
            b=a
            a=-1
        if keys[pygame.K_RIGHT]:
            player.x = player_x + player_width
            player.y = player_y
            b=a
            a=1

        # Spawn apples
        if frame_count % apple_frequency == 0:
            frame_count = 0
            apple_y = [((screen_width // 2) + player_width, 0), (screen_width // 2, 0), ((screen_width // 2) - player_width, 0)]
            apple_x = [(0, screen_height - (player_height // 2)), (0, screen_height - (player_height * 1.5))]
            apple__x = [(screen_width, screen_height - (player_height // 2)), (screen_width, screen_height - (player_height * 1.5))]
            rand = random.randint(0, 6)
            if rand < 2:
                apple_xy = apple__x[rand]
            elif rand < 4:
                apple_xy = apple_x[rand - 2]
            else:
                apple_xy = apple_y[rand - 4]
            apple = pygame.Rect(apple_xy[0] - (apple_width // 2), apple_xy[1] - (apple_height // 2), apple_width, apple_height)
            if rand < 2:
                apples__x.append(apple)
            elif rand < 4:
                apples_x.append(apple)
            else:
                apples_y.append(apple)
            if apple_frequency > 60:
                apple_frequency -= 5
                apple_speed = 6 + int((180 - apple_frequency) * 0.05)

        # Move apples
        for apple in apples_y[:]:
            apple.y += apple_speed
            if apple.top > screen_height:
                apples_y.remove(apple)
                score += 1
        for apple in apples_x[:]:
            apple.x += apple_speed
            if apple.left > screen_width:
                apples_x.remove(apple)
                score += 1
        for apple in apples__x[:]:
            apple.x -= apple_speed
            if apple.right < 0:
                apples__x.remove(apple)
                score += 1

        # Check for collisions
        
        for apple in apples_x:
            if player.colliderect(apple):
                apples_x.remove(apple)
                if input[22] < score:
                    input[22] = score
                input[12]+=score
                input[15] = (input[15] + score)
                score=0
        for apple in apples_y:
            if player.colliderect(apple):
                apples_y.remove(apple)
                if input[22] < score:
                    input[22] = score
                input[12]+=score
                input[15] = (input[15] + score)
                score=0
        for apple in apples__x:
            if player.colliderect(apple):
                apples__x.remove(apple)
                if input[22] < score:
                    input[22] = score
                input[15] = (input[15] + score)
                input[12]+=score
                score=0
        
        if (pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0]<100 and pygame.mouse.get_pos()[1]<100) or keys[pygame.K_ESCAPE]:
            input = [str(int(item))+"\n" for item in input]
            with open("data.txt", "w") as file:
                 file.writelines(input)
            return 3
    
        

            
        if b!=2 and a!=b:
            if a==0:
                player_image=pygame.transform.flip(player_image,True,False)
                flip=not flip
            elif a==-1 and not flip:
                player_image=pygame.transform.flip(player_image,True,False)
                flip=not flip
            elif a==1 and flip:
                player_image=pygame.transform.flip(player_image,True,False)
                flip=not flip
            
            
            
            
            
            
        # Draw everything
        screen.blit(pozadi,(0,0))
        text=font.render(str(score),True ,(0,0,0))
        screen.blit(text,(900,120))
        screen.blit(player_image, (player.x, player.y))
        for apple in apples_x:
            screen.blit(apple_image, (apple.x, apple.y))
        for apple in apples_y:
            screen.blit(apple_image, (apple.x, apple.y))
        for apple in apples__x:
            screen.blit(apple_image, (apple.x, apple.y))

        # Update display
        pygame.display.flip()
        clock.tick(60)
        frame_count += 1
