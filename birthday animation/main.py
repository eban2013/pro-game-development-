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

run=True
while run:
    screen.blit(birthday,(0,0))
    pygame.display.update()
    time.sleep(4)
    screen.blit(baloons,(0,0))
    pygame.display.update()
    time.sleep(4)
    screen.blit(present,(0,0))
    pygame.display.update()
    time.sleep(4)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    
    
    