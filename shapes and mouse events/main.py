import pygame
import random
pygame.init()

WIDTH=800
HEIGHT=800

display=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("shapes and drawing")

run=True
d_colour=["red","green","blue","yellow","white","pink","orange"]
colour="grey"

font=pygame.font.SysFont("calibri",30,)


while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type==pygame.MOUSEMOTION:
            mouse_pos=pygame.mouse.get_pos()
            pygame.draw.circle(display,colour,mouse_pos,10)
        if event.type==pygame.MOUSEBUTTONDOWN:
            colour=random.choice(d_colour)
            txt=font.render("",True,colour)
            display.blit(txt,(20,20))
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            txt=font.render(colour,True,colour)
            display.blit(txt,(20,20))
            pygame.display.update()
            

