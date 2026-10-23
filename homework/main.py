
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

start = None
end = None
running = True

screen.fill("white")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            start = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            end = pygame.mouse.get_pos()
            pygame.draw.line(screen, "black", start, end, 3)
            

    #screen.fill("white")

    # if start != None and end != None:
    #     pygame.draw.line(screen, "black", start, end, 3)

    pygame.display.update()

pygame.quit()
