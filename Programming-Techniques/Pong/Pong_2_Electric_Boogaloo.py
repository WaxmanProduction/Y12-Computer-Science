import pygame
import random
import time
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)

# -- Initialise PyGame
pygame.init()
pygame.font.init()

# -- Manages screen refresh
clock = pygame.time.Clock()

# -- Sets screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Window title
pygame.display.set_caption("Pong 2: Electric Boogaloo")

game_over = False

colours = [GREEN, YELLOW, BLUE, WHITE, RED]
colour = colours[random.randint(0,3)]

right = 0
left = 0

ball_x = 320 # x position
ball_y = 200 # y position
x_speed = 3
y_speed = 3
acceleration = 0

paddle_l = 200
paddle_r = 200

### -- Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #endif
    #next event

    # -- Game logic
    
    # -- Ball movement
    
    ball_x += x_speed
    ball_y += y_speed
    if ball_y > 470 or ball_y < 0:
        y_speed *= -1
    if ball_x > 640:
        ball_x = 320
        ball_y = 200
        paddle_l = 200
        paddle_r = 200
        acceleration = 0
        x_speed = 3
        y_speed = 3
        time.sleep(1)
        left += 1
    elif ball_x < -5:
        ball_x = 320
        ball_y = 200
        paddle_l = 200
        paddle_r = 200
        acceleration = 0
        x_speed = 3
        y_speed = 3
        time.sleep(1)
        right += 1
        

    # Paddle Collision
    if (ball_x < 10 and ball_y > paddle_l and ball_y < paddle_l + 80) or (ball_x > 620 and ball_y > paddle_r and ball_y < paddle_r + 80):
        x_speed *= -1
        acceleration += 1
        if acceleration == 5:
            if x_speed > 0:
                x_speed += 1
            elif x_speed < 0:
                x_speed -= 1
            if y_speed > 0:
                y_speed += 1
            elif y_speed <0:
                y_speed -= 1
            acceleration = 0

    # -- Paddle Controls
    keys = pygame.key.get_pressed()
    # Right Paddle
    if keys[pygame.K_UP]:
        paddle_r -= 5
    elif keys[pygame.K_DOWN]:
        paddle_r += 5
    # Left Paddle
    if keys[pygame.K_w]:
        paddle_l -= 5
    elif keys[pygame.K_s]:
        paddle_l += 5

    # Score Counter
    basicfont = pygame.font.SysFont(None, 72)
    left_score = basicfont.render(str(left), True, colour)
    right_score = basicfont.render(str(right), True, colour)
    
    # -- Background
    screen.fill (BLACK)
    screen.blit(left_score, (60,30))
    screen.blit(right_score, (560,30))

    # -- Objects
    pygame.draw.rect(screen, colour, (ball_x, ball_y, 10, 10))
    pygame.draw.rect(screen, colour, (0, paddle_l, 10, 80))
    pygame.draw.rect(screen, colour, (630, paddle_r, 10, 80))

    # -- Flipping display to change object position
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)

#endwhile

pygame.quit()
