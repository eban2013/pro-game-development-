import pygame 
import time 
pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill('green')

birthday=pygame.image.load(r"C:\Users\User\OneDrive\Documents\thomas jet learn coding\pro game development\birthday animation\imadges\birthday.jpg")
baloons=pygame.image.load(r"C:\Users\User\OneDrive\Documents\thomas jet learn coding\pro game development\birthday animation\imadges\baloons.jpg")
present=pygame.image.load(r"C:\Users\User\OneDrive\Documents\thomas jet learn coding\pro game development\birthday animation\imadges\present.jpg")
images=[birthday,baloons,present]
imadge_no=0

font=pygame.font.SysFont("comic sans",48,)
txt=font.render("Happy Birthday",True,"red")

starttime=pygame.time.get_ticks()
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    screen.blit(images[imadge_no],(0,0))
    screen.blit(txt,(125,125))
    pygame.display.update()
    current_time=pygame.time.get_ticks() 
    if current_time-starttime>=4000:
        imadge_no=imadge_no+1
        starttime=current_time
    if imadge_no==len(images):
        imadge_no=0
    
    