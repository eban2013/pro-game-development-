import pygame 

pygame.init()

WIDTH=500
HIGHT=500

run=True

screen = pygame.display.set_mode((WIDTH,HIGHT))

bg=pygame.image.load(r"C:\Users\User\OneDrive\Documents\thomas jet learn coding\pro game development\cherecters and key events\space bg.png")
ship=pygame.image.load(r"C:\Users\User\OneDrive\Documents\thomas jet learn coding\pro game development\cherecters and key events\rocket charecter.png")

shiprec=pygame.Rect(150,150,150,290)

while run:
     
     screen.blit(bg,(0,0))
     screen.blit(ship,(shiprec.x,shiprec.y))

     pygame.display.update()

     for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                shiprec.y=shiprec.y-5
                
    

pygame.quit()