import pygame

class Bat(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        spriteSize = 48

        
        self.image = pygame.transform.scale(pygame.image.load("sprite1.png"), (spriteSize,spriteSize))
        self.rect = self.image.get_rect()
       
        
        
        self.flap2 = pygame.transform.scale(pygame.image.load("sprite2.png"), (spriteSize,spriteSize))
        self.flap3 = pygame.transform.scale(pygame.image.load("sprite3.png"), (spriteSize, spriteSize))
        self.flap4 = pygame.transform.scale(pygame.image.load("sprite4.png"), (spriteSize, spriteSize))
        self.flap5 = pygame.transform.scale(pygame.image.load("sprite5.png"), (spriteSize, spriteSize))
        self.dead = pygame.transform.scale(pygame.image.load("deadSprite.png"), (spriteSize, spriteSize))

        #self.flap2 = pygame.transform.scale(self.flap2, (64,64))
        
        self.rect.x = x
        self.rect.y = y
        
        self.changeY = 0
    def changeSpeed(self,isMoving):
        if isMoving == True:
            self.changeY -= 1
        else:
            self.changeY = 0
    def update(self,canUpdate):
        #changing update
        if canUpdate == True:
            self.rect.y += self.changeY +5
        else:
            self.changeY = 0


#Initialisation
pygame.init()

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
#game loop
canUpdate = True
gameExit = True
while gameExit == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=True
    #movement
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
    if bat1.rect.y > displayHeight:
        bat1.image = bat1.dead
        canUpdate = False
    print(bat1.rect.y)
    #in this block of code above it is the basis for movement
    screen.fill((0,0,0))
    
    batGroup.draw(screen)
    batGroup.update(canUpdate)
    
    pygame.display.update()
    clock.tick(30)
pygame.quit()#this quits pygame and quits python
quit()


