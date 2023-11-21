import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
open = True

while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.display.update()


