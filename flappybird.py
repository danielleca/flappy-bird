import pygame, sys
pygame.init()
flying=False
gameover=False
fps=60
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,750))
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
bird=Bird(100,400)
birdgrp=pygame.sprite.Group()
birdgrp.add(bird)
while True:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    screen.blit(ground,(groundscroll,600))
    birdgrp.draw(screen)
    birdgrp.update()
    groundscroll-=3
    if abs(groundscroll)>35:
        groundscroll=0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and gameover==False:
            flying=True
    pygame.display.update()
