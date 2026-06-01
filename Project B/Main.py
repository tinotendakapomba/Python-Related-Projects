import pygame
from pygame.locals import *
from random import randint

pygame.init()
black =(0,0,0) 

def warship_movement (warship_list):
    for item in warship_list:
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                item.x +=2
            if event.key == K_LEFT:
                 item.x -=2

def score ():
    current_time = int(pygame.time.get_ticks())-start_game
    font = pygame.font.SysFont(None,48)
    active = font.render("SCORE:"f'{current_time}',True,black )
    rectx = active.get_rect()
    rectx.topleft = (0,0)
    screen.blit(active, rectx)

def warship_attack  ():
    if event.type == KEYDOWN:
        if event.key == K_q:
            miso1 = pygame.image.load("miso1.png")
            miso1.convert_alpha()
            rect6= miso1.get_rect()
            rect6.bottomleft = (x , 472)
            screen.blit(miso1, rect6)





def collisions ():
    pass

def enemy_movement (enemy_list):
    for aliens in enemy_list:
        aliens.y +=1
        if aliens.y >= 800:
            aliens.y = -200



w = 1300
h = 650
x = 50
y= 600

#x =  300
screen = pygame.display.set_mode((w,h))

space = pygame.image.load("space1.jpg")
space.convert_alpha()
Rect = space.get_rect()
Rect.topleft = (0,0)

warship = pygame.image.load("warship.png")
warship.convert_alpha()
rect1 = warship.get_rect()
rect1.bottomleft = (x,y)

enemy1 = pygame.image.load("enemy1.png")
enemy1.convert_alpha()
rect2 = enemy1.get_rect()
rect2.bottomleft = (50,200)

enemy2 = pygame.image.load("enemy2.png")
enemy2.convert_alpha()
rect3 = enemy2.get_rect()
rect3.bottomleft = (350,200)

enemy3 = pygame.image.load("enemy3.png")
enemy3.convert_alpha()
rect4 = enemy3.get_rect()
rect4.bottomleft = (650,200)

enemy4 = pygame.image.load("enemy4.png")
enemy4.convert_alpha()
rect5= enemy4.get_rect()
rect5.bottomleft = (950,200)




pygame.display.update()
pygame.display.flip

warship_timer = pygame.USEREVENT+1
pygame.time.set_timer(warship_timer,400)

game_state =   True
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == warship_timer and game_state:
            if randint(0,2):
                enemy_list.append(enemy1.get_rect(bottomleft =( 50 ,randint(200,400))))
            elif randint(0,3):
                enemy_list.append(enemy2.get_rect(bottomleft =( 350 ,randint(200,400))))
            elif randint(0,4):
                enemy_list.append(enemy3.get_rect(bottomleft =( 650 ,randint(200,400))))
            elif randint(0,5):
                enemy_list.append(enemy4.get_rect(bottomleft =( 950 ,randint(200,400))))

          
        

        

        

    warship_list = [rect1]
    warship_movement(warship_list)
    enemy_list = [rect2,rect3,rect4,rect5]
    enemy_movement(enemy_list)
    start_game = int(pygame.time.get_ticks())
    score ()
    warship_attack()

 


    

    if game_state :

        screen.blit(space,Rect)
        screen.blit(warship, rect1)
        screen.blit(enemy1, rect2)
        screen.blit(enemy2, rect3)
        screen.blit(enemy3, rect4)
        screen.blit(enemy4, rect5)
        pygame.display.update()
        pygame.display.flip


    else:
        screen.fill(0,0,255)
        pygame.display.update()
        pygame.display.flip

        



            

