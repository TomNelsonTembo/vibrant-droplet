import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
open = True
pygame.display.set_caption('Runner 2D')
clock = pygame.time.Clock()
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load ('graphics/ground.png')
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = test_font.render('Runner 2D', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600


player_surface = pygame.image.load('graphics/Player/player_walk_1.png')
player_x_pos = 50

while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    snail_x_pos -= 3
    if snail_x_pos <= -100:
        snail_x_pos = 800
        
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, (snail_x_pos, 263))
    screen.blit(player_surface, (player_x_pos, 217))
    pygame.display.update()
    clock.tick(60)


