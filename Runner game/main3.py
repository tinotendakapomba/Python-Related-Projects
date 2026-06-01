import pygame
from pygame.locals import *
from random import randint, choice

class User (pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.player =pygame.image.load("player.png").convert_alpha()
        self.player2 = pygame.image.load("player2.png").convert_alpha()
        self.player_walk = [pygame.image.load("player.png").convert_alpha(),pygame.image.load("player2.png").convert_alpha()]
        self.player_index = 0
        self.player_jump = pygame.image.load("player.png").convert_alpha()
        self.image = pygame.image.load("player.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(bottomright = (250,p))
        self.gravity =  0

       # self.jump_sound = pygame.mixer.Sound("dior.mp3")
        #self.jump_sound.set_volume(0.4)

        

    def player_input (self):
        
        if event.type == KEYDOWN:
            if event.key == K_UP and p >= 350:
                self.gravity = -22

        if event.type == MOUSEBUTTONDOWN and p >= 350:
                self.gravity = -22
                #self.jump_sound.play()


    def apply_gravity(self):
        self.gravity += 1 
        self.rect.y += self.gravity
        if self.rect.bottom >= 450:
            self.rect.bottom = 450

    def animation_state (self):
        if self.rect.bottom <450:
            self.image = self.player_jump
        else: 
            self.player_index += 0.2
            if self.player_index >= len (self.player_walk):self.player_index = 0
            self.image =  self.player_walk [int(self.player_index)]
    def update (self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

    
class Obsticles (pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == "thorn1":
            thorn1 =pygame.image.load("thorn1.png").convert_alpha()
            self.frames = [thorn1]
            y_pos = 460
            
        else:
            thorn4 =pygame.image.load("thorn4.png").convert_alpha()
            self.frames = [thorn4]
            y_pos = 300


        self.animation_index =0 
        self.image =   self.frames [self.animation_index]
        self.rect = self.image.get_rect(bottomright = (randint (1150,1200),y_pos))

    def update(self,) :
        self.rect.x -= 7
        self.destroy()

    def destroy (self):
        if self.rect.x  <= -100:
            self.kill








# the code below is for showing the score while game state is true
def score ():
    global current_time
    current_time = int(pygame.time.get_ticks()/500)-start_time
    font = pygame.font.SysFont(None,30)
    img1 = font.render( "SCORE:"f'{current_time}' ,True , RED) 
    rect0 = img1.get_rect()
    rect0.topleft = (0,5)
    screen.blit(img1,rect0)


# the function bellow  moves obsticles that are in the list whilst deleting those that are off the screen
def obsticle_movement (obsticle_rect_list):
    if obsticle_rect_list:
        for obsticle_rect in obsticle_rect_list:
            obsticle_rect.x -= 7  
            if obsticle_rect.bottom == 460:
                screen.blit(thorn1,obsticle_rect)
            else:
                screen.blit(thorn4,obsticle_rect)
        obsticle_list = [obsticle for obsticle in obsticle_rect_list if obsticle_rect.x >-100]
        return obsticle_rect_list 
    else:
        return[]
        

# for collisions of player with the obsticles in his path
def collision (player,obsticle_rect_list):
    if obsticle_rect_list:
        for obsticle_rect in obsticle_rect_list:
            if player.colliderect(obsticle_rect):return False

    else:
        return True

def collision_sprite ():
    if pygame.sprite.spritecollide(user.sprite,obsticle_group, True):
        obsticle_group.empty()
        return False
    else:
        return True





pygame.init()
screen = pygame.display.set_mode((1095,700)) 
pygame.display.set_caption("Runner")

#bg_music =  pygame.mixer.Sound("dior.mp3")
#bg_music.play(loop = -1)
start_time = 0
clock = pygame.time.Clock()
RED = (125,0,0)
GRAY = (125,125,125)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GREEN = (0,255,0)
CYAN = (0, 255, 255)

BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)

x = 800
z = 1300
w = 1800
p= 450
screen.fill(GRAY)

sky =pygame.image.load("sky.jpg")
sky.convert_alpha()
rect2 = sky.get_rect()
rect2.bottomleft = (0,450)

ground =pygame.image.load("ground.jpg")
ground.convert_alpha()
rect1 = ground.get_rect()
rect1.topleft = (0,450)

thorn1 =pygame.image.load("thorn1.png")
thorn1.convert_alpha()
rect3 = thorn1.get_rect()

thorn4 =pygame.image.load("thorn4.png")
thorn4.convert_alpha()
rect4 = thorn4.get_rect()

obisticle_rect_list = []



player =pygame.image.load("player.png")
player2 = pygame.image.load("player2.png")
player2.convert_alpha()
player.convert_alpha()
player_walk = (player,player2)
player_jump = pygame.image.load("player.png").convert_alpha()
player_index = 0
player_surface = player_walk[player_index]
rect = player2.get_rect()
rect = player.get_rect()
rect.bottomright = (200,p)





user = pygame.sprite.GroupSingle()
user.add(User())

obsticle_group = pygame.sprite.Group()
gravity = 0
impact = False
running = True
game_state = True

#timer
obsticle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obsticle_timer,2000)



while running:
    for event in pygame.event.get():

        if event.type== QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_UP and p >= 350:
                gravity = -28

        if event.type == MOUSEBUTTONDOWN and p >= 350:
                gravity = -28

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                game_state = True
            
                start_time = int(pygame.time.get_ticks()/500)

# the code bellow puts the obsticles in a list and assign them position and make them appear at random 
                
        if event.type == obsticle_timer and game_state:
            obsticle_group.add(Obsticles(choice([" thorn1" ,"thorn1","thorn1" ,"thorn4" ])))
           # if randint (0,2):
            #    obisticle_rect_list.append(thorn1.get_rect(bottomright = (randint (1150,1200),460)))
            #else:
             #   obisticle_rect_list.append(thorn4.get_rect(bottomright = (randint (1150,1200),300)))


            
    if game_state:


        game_state = collision(rect,obisticle_rect_list)
        screen.blit(sky,rect2)
        screen.blit(ground,rect1)

        user.draw(screen)
        user.update()
        obsticle_group.draw(screen)
        obsticle_group.update()
                
        rect2.bottomleft = (0,450)
        rect1.topleft = (0,450)
        game_state = collision_sprite()

        score()
  
       
    else:
        obisticle_rect_list.clear()
        screen.fill(RED)
        font1 = pygame.font.SysFont(None , 46)
        img1 = font1.render("GAME OVER" , True ,CYAN )

        rect7 = img1.get_rect()
        rect7.center = (540,600)

        font4 = pygame.font.SysFont(None , 48)
        img4 = font4.render("RUNNER" , True ,GREEN)

        rect8 = img4.get_rect()
        rect8.midtop = (550,50)
        screen.blit(img4,rect8)


        player =pygame.image.load("player.png")
        player.convert_alpha
        rect9 = player.get_rect()
        rect9.center = (540,300)
        screen.blit(player,rect9)


        xyz = font4.render("your score is:"f"{current_time}",True,GREEN)
        rect10 = xyz.get_rect()
        rect10.midtop = (540,450)
        screen.blit (xyz,rect10)

        screen.blit(img1,rect7)


    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

