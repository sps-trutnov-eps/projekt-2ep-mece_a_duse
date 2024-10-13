import pygame
import random

def agility():
    pygame.init()

    # Screen dimensions
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Load images
    player_image = pygame.image.load('sprites/hrac sam.png')
    apple_image = pygame.image.load('sprites/apple.png')

    # Scale images
    player_image = pygame.transform.scale(player_image, (50, 50))
    apple_image = pygame.transform.scale(apple_image, (30, 30))

    # Colors
    white = (255, 255, 255)

    # Player settings
    player_width = player_image.get_width()
    player_height = player_image.get_height()
    player_x = screen_width // 2
    player_y = screen_height - player_height - 10
    player_speed = 5

    # Apple settings
    apple_width = apple_image.get_width()
    apple_height = apple_image.get_height()
    apple_speed = 5
    apple_frequency = 50

    # Initialize player and apple positions
    player = pygame.Rect(player_x, player_y, player_width, player_height)
    apples_x = []
    apples_y = []
    apples__y = []

    # Game loop control
    clock = pygame.time.Clock()
    score = 0

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.y -= player_speed
        if keys[pygame.K_DOWN]:
            player.y += player_speed
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        # Spawn apples
        if random.randint(1, apple_frequency) == 1:
            apple_x = [(player_height // 2, player_width // 2), (player_height // 2, (player_width // 2) + player_width)]
            apple_y = [(screen_height - (player_height // 2), (player_width // 2)), (screen_height - (player_height * 1.5), screen_width - (player_width // 2)), (player_height // 2, (player_width * 1.5))]
            apple__y = [(screen_height - (player_height // 2), screen_width - (player_width // 2)), (screen_height - (player_height * 1.5), screen_width - (player_width // 2))]
            rand = random.randint(0, 5)
            if rand < 2:
                apple_xy = apple__y[rand]
            elif rand < 4:
                apple_xy = apple_y[rand - 2]
            else:
                apple_xy = apple_x[rand - 4]
            apple = pygame.Rect(apple_xy[0], apple_xy[1], apple_width, apple_height)
            if rand < 2:
                apples__y.append(apple)
            elif rand < 4:
                apples_y.append(apple)
            else:
                apples_x.append(apple)

        # Move apples
        for apple in apples_x[:]:
            apple.x += apple_speed
            if apple.top > screen_height:
                apples_x.remove(apple)
                score += 1
        for apple in apples_y[:]:
            apple.y += apple_speed
            if apple.left > screen_width:
                apples_y.remove(apple)
                score += 1
        for apple in apples__y[:]:
            apple.y -= apple_speed
            if apple.right < 0:
                apples__y.remove(apple)
                score += 1

        # Check for collisions
        for apple in apples_x:
            if player.colliderect(apple):
                return 3
        for apple in apples_y:
            if player.colliderect(apple):
                return 3
        for apple in apples__y:
            if player.colliderect(apple):
                return 3

        # Draw everything
        screen.fill(white)
        screen.blit(player_image, (player.x, player.y))
        for apple in apples_x:
            screen.blit(apple_image, (apple.x, apple.y))
        for apple in apples_y:
            screen.blit(apple_image, (apple.x, apple.y))
        for apple in apples__y:
            screen.blit(apple_image, (apple.x, apple.y))

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

agility()

