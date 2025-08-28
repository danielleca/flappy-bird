import pygame, sys
pygame.init()
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
    def __init__(self):
        super().__init__()
        self.images=[]
        self.index=0
        for i in range(1,4):
            img=pygame.image.load(f"bird{i}.png")
            self.images.append(img)
        self.image=self.images[self.index]
while True:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    screen.blit(ground,(groundscroll,600))
    groundscroll-=3
    if abs(groundscroll)>35:
        groundscroll=0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
