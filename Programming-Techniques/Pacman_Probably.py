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

# -- Manages screen refresh
clock = pygame.time.Clock()

# -- Sets screen
size = (560,620)
screen = pygame.display.set_mode(size)

# -- Window title
pygame.display.set_caption("PAC MAN")

game_over = False

# == Define Classes -- #

# -- Defines Walls
class Tile(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, x_ref, y_ref):
            super().__init__()
            self.image = pygame.Surface([width,height])
            self.image.fill(colour)
            self.rect = self.image.get_rect()
            self.rect.x = x_ref
            self.rect.y = y_ref
    #End Public Procedure
#End Class

class Player(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, x_ref, y_ref):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed = 0
    #End Public Procedure

    def update(self):
       self.rect.x += self.speed
    #End Public Procedure

    def player_set_speed(self,val):
        speed = val
        if speed == -3:
            self.speed += -3
        elif speed == 3:
            self.speed = +3
        elif speed == 0:
            self.speed = 0

    #End Public Procedure


map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
       [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
       [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
       [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
       [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
       [0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0],
       [0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0],
       [0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0],
       [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
       [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1],
       [0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0],
       [0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0],
       [0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0],
       [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1],
       [1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1],
       [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
       [1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
       [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
       [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
       [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
       [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
       [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

all_sprites_group = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

pacman = Player(YELLOW,10,10,200,30)

all_sprites_group.add(pacman)

for x in range(28):
    for y in range (31):
        if map[y][x] == 1:
            my_wall = Tile(BLUE, 20, 20, x*20, y*20)
            wall_list.add(my_wall)
            all_sprites_group.add(my_wall)



### -- Game Loop -- ###
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player.player_set_speed(pacman,-3)
            elif event.key == pygame.K_RIGHT:
                Player.player_set_speed(pacman,3)
            elif event.key == pygame.K_UP:
                Player.player_set_speed(pacman,0)
            elif event.key == pygame.K_DOWN:
                Player.player_set_speed(pacman,0)
        #endif
    #next event


    # -- Draw the stuff
    all_sprites_group.draw(screen)

    # -- Flipping display to change object position
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)

pygame.quit()
