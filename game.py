import pygame
import random
from guizero import App,PushButton

class Bat(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        spriteSize = 48

        self.image = pygame.transform.scale(pygame.image.load("sprite2.png"), (spriteSize,spriteSize))
        self.rect = self.image.get_rect()       

        self.flap2 = pygame.transform.scale(pygame.image.load("sprite2.png"), (spriteSize,spriteSize))
        self.flap3 = pygame.transform.scale(pygame.image.load("sprite3.png"), (spriteSize, spriteSize))
        self.dead = pygame.transform.scale(pygame.image.load("deadSprite.png"), (spriteSize, spriteSize))

        self.rect.x = x
        self.rect.y = y

        self.changeX = 0
        self.changeY = 0

    def changeSpeed(self,isMoving,isDead):
        if isDead == False:
            if isMoving == True:
                self.changeY -= 1
            if isMoving == False:
                self.changeY +=.9
        elif isDead == True:
            self.changeY = 0
        self.rect.y += self.changeY
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
        if self.rect.x <-40:
            self.kill()


def play():
        app.hide()
        pygame.init()
        score = 0
        screen = pygame.display.set_mode((displayWidth,displayHeight))
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None,25)
        #scoreBoardFont = pygame.font.Font("plank.ttf",25)
        bat1 = Bat(100,100)
        batGroup = pygame.sprite.Group()
        batGroup.add(bat1)

        wallTop = Wall(50,-800,40,1000)
        wallBot = Wall(50,300,40,1000)
        wallGroup = pygame.sprite.Group()
        wallGroup.add(wallTop)
        wallGroup.add(wallBot)

        isDead = False
        pressed = False
        gameExit = True
        while gameExit == True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=False
                #movement
                if (bat1.rect.y < displayHeight-19):
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pressed = True
                            bat1.image = bat1.flap3
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            pressed = False
                            bat1.image = bat1.flap2

            if bat1.rect.y > displayHeight-15:
                isDead=True
                bat1.rect.y = displayHeight-15    
                bat1.image = bat1.dead
                bat1.changeSpeed(False,isDead)
                pygame.quit()
                app.show()

            pipeCollide = pygame.sprite.spritecollide(bat1, wallGroup, False)
            if pipeCollide:
                isDead= True
                bat1.image = bat1.dead
                bat1.rect.y = displayHeight-15
                bat1.changeSpeed(False,isDead)
                canUpdate = False
                pygame.quit()
                app.show()

            ycoord = random.randint(100,300)
            if wallTop.rect.x < -40:
                wallTop = Wall(50,ycoord - 1000,40,1000)
                wallBot = Wall(50,wallTop.rect.y + 1075,40,1000)
                wallGroup.add(wallTop)
                wallGroup.add(wallBot)
                score+=1
            screen.fill((0,0,0))
            screenText = font.render(str(score),True,((255,0,0)))
            screen.blit(screenText,[20,10])
            batGroup.draw(screen)
            wallGroup.draw(screen)
            wallGroup.update()
            bat1.changeSpeed(pressed,isDead)
            pygame.display.update()
            clock.tick(30)

def quit():
    exit()


displayWidth = 288
displayHeight = 512
app = App()
button = PushButton(app,command = play, text = "play")
button = PushButton(app,command = quit, text = "exit")
app.display()
