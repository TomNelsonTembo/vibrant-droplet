import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
open = True
pygame.display.set_caption('Runner 2D')
clock = pygame.time.Clock()
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load ('graphics/ground.png').convert()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = test_font.render('Runner 2D', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (900, 300))



player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (50, 300))









while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    snail_rect.left -= 3
    if snail_rect.right <= -100:
        snail_rect.right = 900
        
    print(player_rect.left)
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    pygame.display.update()
    clock.tick(60)


