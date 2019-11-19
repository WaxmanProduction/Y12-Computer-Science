import pygame
import random
import math

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)

# -- Initialise PyGame
pygame.init()

# -- Manages screen refresh
clock = pygame.time.Clock()

# -- Sets screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Window title
pygame.display.set_caption("Space Invaders")


class Invader(pygame.sprite.Sprite):
    def __init__(self,color,width,height,speed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,600)
        self.rect.y = random.randrange(-50,0)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class Player(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 450
        self.speed = 0
    #End Public Procedure (constructor)

    def update(self):
       self.rect.y += self.speed
    #End Public Procedure
       
    def player_set_speed(val):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player.player_set_speed(-3)
            elif event.key == pygame.K_RIGHT:
               Player.player_set_speed(3) 
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player.player_set_speed(0)
   
    #End Public Procedure

#EndClass



game_over = False
invader_group = pygame.sprite.Group()
my_player = Player(RED, 20, 10)

all_sprites_group = pygame.sprite.Group()

all_sprites_group.add(my_player)

flakes_num = 15
for x in range (flakes_num):
    my_invader = Invader(WHITE, 10, 10, 1)
    invader_group.add(my_invader)
    all_sprites_group.add(my_invader)
    

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player.player_set_speed(-3)
            elif event.key == pygame.K_RIGHT:
               Player.player_set_speed(3) 
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player.player_set_speed(0)
   
    all_sprites_group.update()
    
    
    screen.fill(BLACK)
    
    all_sprites_group.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
