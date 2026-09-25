import pygame 
pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill('green')

birthday=pygame.image.load(r"C:\Users\User\OneDrive\Documents\thomas jet learn coding\pro game development\birthday animation\imadges\birthday.jpg")

run=True
while run:
    screen.blit(birthday,(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    
    
    