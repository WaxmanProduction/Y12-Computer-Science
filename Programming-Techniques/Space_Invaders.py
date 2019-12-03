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
pygame.display.set_caption("Space Invaders")


# -- Fonts == #
basicfont = pygame.font.SysFont(None, 36)

# -- Classes -- #

# -- Creates invaders
class Invader(pygame.sprite.Sprite):
    def __init__(self,colour,width,height,speed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10,630)

        self.rect.y = random.randrange(-50,0)
        self.speed = speed
    #End Public Procedure

    def update(self):
        self.rect.y += self.speed
    #End Public Procedure

# EndClass

# -- Creates player
class Player(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 450
        self.speed = 0
    #End Public Procedure

    def update(self):
       self.rect.x += self.speed
    #End Public Procedure

    def player_set_speed(self,val):
        speed = val
        if speed == -3:
            if self.rect.x > 620:
                self.speed = -3
            else:
                self.speed += -3
        elif speed == 3:
            if self.rect.x < 0:
                self.speed = +3
            else:
                self.speed += 3
        elif speed == 0:
            self.speed = 0
    #End Public Procedure


        
#EndClass

class Bullet(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
    #End Public Procedure

    def update(self):
        self.rect.y -= 5
    #End Public Procedure

class Invader_bullet(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
    #End Public Procedure

    def update(self):
        self.rect.y += 5
    #End Public Procedure
        
score = 0     
lives = 5
bullet_count = 50
    

game_over = False

bullet_group = pygame.sprite.Group()
invader_group = pygame.sprite.Group()
invader_attacks = pygame.sprite.Group()
hero = Player(RED, 20, 10)


all_sprites_group = pygame.sprite.Group()

all_sprites_group.add(hero, invader_attacks)


for _ in range (60):
    invader = Invader(WHITE, 10, 10, 1)
    invader_group.add(invader)
    all_sprites_group.add(invader)
    

clock = pygame.time.Clock()

### -- Game Loop -- ###

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player.player_set_speed(hero,-3)
            elif event.key == pygame.K_RIGHT:
               Player.player_set_speed(hero,3)
            elif event.key == pygame.K_UP and bullet_count != 0:
                bullet = Bullet(RED,5,10)
                bullet.rect.x = hero.rect.x + 7
                bullet.rect.y = hero.rect.y
                all_sprites_group.add(bullet)
                bullet_group.add(bullet)
                bullet_count -= 1
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player.player_set_speed(hero,0)

    # == Counters
    score_counter = basicfont.render("Score = " + str(score), True, WHITE)
    bullet_counter = basicfont.render("Bullets Remaining = " + str(bullet_count), True, WHITE)
    life_counter = basicfont.render(str(lives) + " lives", True, WHITE)

    all_sprites_group.update()

    for bullet in bullet_group:
        if pygame.sprite.spritecollide(bullet, invader_group, True):
            bullet_group.remove(bullet)
            all_sprites_group.remove(bullet)
            score += 1
        elif bullet.rect.y < -10:
            bullet_group.remove(bullet)
            all_sprites_group.remove(bullet)

    player_hit_group = pygame.sprite.spritecollide(hero, invader_group, True)
    
    # -- Background
    screen.fill(BLACK)
    screen.blit(score_counter, (20,20))
    screen.blit(bullet_counter, (20,45))
    screen.blit(life_counter, (20,70))
    
    all_sprites_group.draw(screen)

    for foo in player_hit_group:
        lives -= 1
        all_sprites_group.remove(hero)
        bullet_count = 0
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
