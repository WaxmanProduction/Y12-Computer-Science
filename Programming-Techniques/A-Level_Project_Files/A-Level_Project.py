import pygame
import random
import math

# -- Colours -- #
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)

# -- Initialise PyGame -- #
pygame.init()

# -- Manages screen refresh -- #
clock = pygame.time.Clock()

# -- Sets screen -- #
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Window title -- #
pygame.display.set_caption("Untitled Game")

# -- Initial variables -- #

clock = pygame.time.Clock()

game_over = False

# -- Classes -- #

class Player(pygame.sprite.Sprite):
    def __init__(self,colour,width,height,speed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 273
        self.rect.y = 463
        self.speed = speed
    #End Public Procedure

    def update(self):
       self.rect.x += self.speed
    #End Public Procedure

#End Class

class Enemy(pygame.sprite.Sprite):
    def __init__(self,colour,width,height,speed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 273
        self.rect.y = 400
        self.speed = speed
    #End Public Procedure

#End Class

class Wall(pygame.sprite.Sprite):
    def __init__(self,colour,width,height,x_ref,y_ref):
            super().__init__()
            self.image = pygame.Surface([width,height])
            self.image.fill(colour)
            self.rect = self.image.get_rect()
            self.rect.x = x_ref
            self.rect.y = y_ref
    #End Public Procedure

#End Class

class Item(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 273
        self.rect.y = 300
    #End Public Procedure

# -- Define Sprites

hero = Player(RED,20,20,0)

all_sprites_group = pygame.sprite.Group()

all_sprites_group.add(hero)

### -- Game Loop -- ###

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # -- Draw the items
    screen.fill(BLACK)

    all_sprites_group.draw()

     # -- Flipping display to change object position
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)

pygame.quit()
