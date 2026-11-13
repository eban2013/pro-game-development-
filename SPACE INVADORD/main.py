import pygame
pygame.init()

WIDTH=1600
HEIGHT=900

run=True

screen=pygame.display.set_mode((WIDTH,HEIGHT))

bg=pygame.image.load(r"C:\Users\User\OneDrive\Documents\thomas jet learn coding\pro game development\SPACE INVADORD\imadges\bg.png")
bg=pygame.transform.scale(bg,(WIDTH,HEIGHT))
ship_size=75
red=pygame.image.load(r"C:\Users\User\OneDrive\Documents\thomas jet learn coding\pro game development\SPACE INVADORD\imadges\red.png")
red=pygame.transform.scale(red,(ship_size,ship_size))
yellow=pygame.image.load(r"C:\Users\User\OneDrive\Documents\thomas jet learn coding\pro game development\SPACE INVADORD\imadges\yellow.png")
yellow=pygame.transform.scale(yellow,(ship_size,ship_size))
red_rect=pygame.Rect(250,HEIGHT/2,ship_size,ship_size)
yellow_rect=pygame.Rect(WIDTH-250,HEIGHT/2,ship_size,ship_size)

NET=pygame.Rect(WIDTH/2-10,0,20,HEIGHT)

while run:

    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"black",NET)
    pygame.display.update()



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()