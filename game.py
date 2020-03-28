import pygame

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
        """ 
        self.rect.y += self.changeY
        blockHitList = pygame.sprite.spritecollide(self, wallGroup, False)
        for block in blockHitList:
                if self.changeX > 0:
                        self.rect.right = block.rect.left
                else:
                        self.rect.left = block.rect.right
                        """
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
wall = Wall(50,10,100,100)
wallGroup.add(wall)
bat1.walls = wallGroup

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
    if bat1.rect.y > displayHeight-19:
        bat1.image = bat1.dead
        canUpdate = False
    print(bat1.rect.y)

    pipeCollide = pygame.sprite.spritecollide(bat1, wallGroup, False)
    if pipeCollide:
            print("touching pipe")
            canUpdate = False


    #in this block of code above it is the basis for movement
    screen.fill((0,0,0))
    
    batGroup.draw(screen)
    batGroup.update(canUpdate)

    wallGroup.draw(screen)
    wallGroup.update()
    
    pygame.display.update()
    clock.tick(30)
pygame.quit()#this quits pygame and quits python
quit()


