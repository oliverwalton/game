import pygame
import time
from random import randint

class Bat(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        spriteSize = 48
        
        self.image = pygame.transform.scale(pygame.image.load("sprite2.png"), (spriteSize,spriteSize))
        self.rect = self.image.get_rect()
        
        # this is where the sprite images are loaded TODO: remove the sprite images that are not necessary
        self.flap2 = pygame.transform.scale(pygame.image.load("sprite2.png"), (spriteSize,spriteSize))
        self.flap3 = pygame.transform.scale(pygame.image.load("sprite3.png"), (spriteSize, spriteSize))
        self.dead = pygame.transform.scale(pygame.image.load("deadSprite.png"), (spriteSize, spriteSize))

        # this is where the starting coordinate is set
        self.rect.x = x
        self.rect.y = y
        
        # this is where the movement mechanic is initailised
        self.changeY = 0
        self.changeX = 0

        self.walls = None
    def changeSpeed(self,isMoving):
    # in this function, it is the mechanic that lets the bat jump TODO: improve the jumping mechanic
        if isMoving == True:
            self.changeY -= 1
        # in this else condition, it is what stops the sprite from moving off the screen so the bat can die
        else:
            self.changeY = 0
    # this update function is where gravity is set TODO: improve gravity feel
    def update(self,canUpdate):
        #changing update
        
        if canUpdate == True:
            self.rect.y += self.changeY +5 
        else:
            self.changeY = 0
            self.image = self.dead
            return False

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = displayWidth +100
        
    def update(self):
        self.rect.x -=3
#Initialisation
pygame.init()

#font = pygame.font.SysFont(None, 25)
#ScoreBoardFont = pygame.font.Font("PLANK___.ttf", 25)

displayWidth=288
displayHeight=512 

pressed = False

screen = pygame.display.set_mode((displayWidth,displayHeight))# creates a screen: 800px600p
pygame.display.update()

clock = pygame.time.Clock()

#object Initialisation
bat1 = Bat(100,100)
batGroup = pygame.sprite.Group()
batGroup.add(bat1)

wallGroup = pygame.sprite.Group()
#wall = Wall(50,10,100,100)
#wallGroup.add(wall)
#              x, y,   w, h
wallTop = Wall(50,-800,40,1000)
wallBot = Wall(50,300,40,1000)
wallGroup.add(wallTop)
wallGroup.add(wallBot)
bat1.walls = wallGroup

#game loop
canUpdate = True
gameExit = True
while gameExit == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=False
    #movement
    if bat1.update(canUpdate) == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed = True
                    bat1.changeSpeed(True)
                    bat1.image = bat1.flap3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pressed = False
                    bat1.changeSpeed(False)
                    bat1.image = bat1.flap2
    if bat1.rect.y > displayHeight-19:
        bat1.image = bat1.dead
        bat1.update(False)
        #canUpdate = False
    print(bat1.rect.y)
    
# this checks to see if the bat is touching the pipe, and if it is, it will die
    pipeCollide = pygame.sprite.spritecollide(bat1, wallGroup, False)
    if pipeCollide:
            bat1.rect.y = displayHeight-19
            bat1.update(False)
            bat1.changeSpeed(False)
            canUpdate = False
            #batGroup.remove(bat1)
            
            



    #in this block of code above it is the basis for movement
    screen.fill((0,0,0))
    batGroup.draw(screen)
    wallGroup.draw(screen)
    wallGroup.update()    
    if bat1.update(canUpdate) == True:
        batGroup.update(canUpdate)
    else:
        pass
    
    pygame.display.update()
    clock.tick(30)
pygame.quit()#this quits pygame and quits python
quit()
