import pygame, sys, random
pygame.init()
flying=False
gameover=False
fps=60
clock=pygame.time.Clock()
W=800
H=750
pipegap=100
scrollspeed=5
lastpipe=pygame.time.get_ticks()
pipefrequency=1500 #miliseconds
screen=pygame.display.set_mode((W,H))
pygame.display.set_caption("flappy bird")
screen.fill("lightpink")
bg=pygame.image.load("background.png")
ground=pygame.image.load("ground.png")
groundscroll=0
pygame.display.update()
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images=[]
        self.index=0
        for i in range(1,4):
            img=pygame.image.load(f"bird{i}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.v=0
        self.click=False
    def update(self):
        if flying==True:
            self.v+=0.5
            #gravity
        if self.v>8:
            self.v=8
        if self.rect.bottom<600:
            
            self.rect.y+=self.v
        self.index+=1
        if self.index>=len(self.images):
            self.index=0
        self.image=self.images[self.index]
        if gameover==False:
            if pygame.mouse.get_pressed()[0]==1 and self.click==False:
                self.click=True
                self.v=-10
            if pygame.mouse.get_pressed()[0]==0:
                self.click=False
            self.image=pygame.transform.rotate(self.images[self.index],20)
        else:
            self.image=pygame.transform.rotate(self.images[self.index],-20)

class Pipe(pygame.sprite.Sprite):
    def __init__(self,pos,x,y):
        super().__init__()
        self.image=pygame.image.load("pipe.png")
        self.rect=self.image.get_rect()
        if pos==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y]
        elif pos==2:
            self.rect.topleft=[x,y]
    def update(self):
        self.rect.x-=scrollspeed
        if self.rect.right<0:
            self.kill()

pipegrp=pygame.sprite.Group()

bird=Bird(100,400)
birdgrp=pygame.sprite.Group()
birdgrp.add(bird)
while True:
    clock.tick(fps)
    screen.blit(bg,(0,0))  
    birdgrp.draw(screen)
    pipegrp.draw(screen)
    screen.blit(ground,(groundscroll,600))
    birdgrp.update()

    if len(pipegrp)>0:
        pass
    if flying==True and gameover==False:
        time=pygame.time.get_ticks()
        if time-lastpipe>pipefrequency:
            pipeheight=random.randint(-80,80)
            toppipe=Pipe(1,W,H/2-pipegap+pipeheight)
            bottompipe=Pipe(2,W,H/2+pipegap+pipeheight)
            pipegrp.add(toppipe)
            pipegrp.add(bottompipe)
            lastpipe=time
    pipegrp.update()
    if flying==True and gameover==False:
        groundscroll-=3
        if abs(groundscroll)>35:
            groundscroll=0
    if bird.rect.bottom>=600:
        gameover=True
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and gameover==False:
            flying=True
    pygame.display.update()
