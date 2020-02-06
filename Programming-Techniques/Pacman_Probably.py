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
    def __init__(self, colour, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 273
        self.rect.y = 463
        self.speedx = 0
        self.speedy = 0
    #End Public Procedure

    def update(self):
       self.rect.x += self.speedx
       self.rect.y += self.speedy
    #End Public Procedure

    def player_set_speed(self,valx,valy):
        self.speedx = valx
        self.speedy = valy
    #End Public Procedure

class Ghost(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 273
        self.rect.y = 222
        self.speedx = 0
        self.speedy = 0
    #End Public Procedure

    def update(self):
       self.rect.x += self.speedx
       self.rect.y += self.speedy
    #End Public Procedure

    def enemy_movement(self,valx,valy):
        self.speedx += valx
        self.speedy += valy
        

maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
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
        [0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0],
        [1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1],
        [0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0],
        [0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0],
        [0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0],
        [1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1],
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
pacman = Player(YELLOW,15,15)
ghost1 = Ghost(RED,15,15)

all_sprites_group.add(pacman, ghost1)

for x in range(28):
    for y in range (31):
        if maze[y][x] == 1:
            my_wall = Tile(BLUE, 20, 20, x*20, y*20)
            wall_list.add(my_wall)
            all_sprites_group.add(my_wall)
        #endif
    #next
#next

### -- Game Loop -- ###
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player.player_set_speed(pacman,-1,0)
            elif event.key == pygame.K_RIGHT:
                Player.player_set_speed(pacman,1,0)
            elif event.key == pygame.K_UP:
                Player.player_set_speed(pacman,0,-1)
            elif event.key == pygame.K_DOWN:
                Player.player_set_speed(pacman,0,1)
            #endif
        #endif
                
    # -- Enemy movement 
    if pacman.rect.x > ghost1.rect.x:
        ghost1.enemy_movement(1,0)
    elif pacman.rect.x < ghost1.rect.x:
        ghost1.enemy_movement(-1,0)
    if pacman.rect.y > ghost1.rect.y:
        ghost1.enemy_movement(0,1)
    elif pacman.rect.y < ghost1.rect.y:
        ghost1.enemy_movement(0,-1)
    #endif


    # -- Map loop
    if pacman.rect.x < -20:
        pacman.rect.x = 635
    elif pacman.rect.x > 640:
        pacman.rect.x = -15
    #endif
        

    # -- Check for collisions between characters and wall tiles
    player_hit_list = pygame.sprite.spritecollide(pacman, wall_list, False)
    enemy_hit_list = pygame.sprite.spritecollide(ghost1, wall_list, False)

    for foo in player_hit_list:
        pacman.player_set_speed(0,0)
        pacman.rect.x = pacman_old_x
        pacman.rect.y = pacman_old_y
    #next

    for foo in enemy_hit_list:
        ghost1.enemy_movement(0,0)
        ghost1.rect.x = ghost1_old_x
        ghost1.rect.y = ghost1_old_y
    #next

    if ghost1.rect.y > (pacman.rect.y - 5) and ghost1.rect.y < (pacman.rect.y + 15) and ghost1.rect.x > pacman.rect.x and ghost1.rect.x < (pacman.rect.x + 10):
        game_over = True
    #endif
        
    # -- Run the update function for all sprites
    pacman_old_x = pacman.rect.x
    pacman_old_y = pacman.rect.y
    ghost1_old_x = ghost1.rect.x
    ghost1_old_y = ghost1.rect.y
    all_sprites_group.update()
        
    # -- Run the update function for all sprites
    all_sprites_group.update()

    # -- Draw the stuff
    screen.fill(BLACK)
    all_sprites_group.draw(screen)
    all_sprites_group.update()

    # -- Flipping display to change object position
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)

#endwhile

pygame.quit()
