import pygame
from random import randint
from os.path import join


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("banana🍌")
running = True

# plane surface
surf = pygame.Surface((50, 50))
surf.fill("red")
x = 50

# importing image rocket
player_surf = pygame.image.load(join('assets', 'images', 'rocket.svg')).convert_alpha()

# importing image star
star_surf = pygame.image.load(join('assets', 'images', 'star.svg')).convert_alpha()

#
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

# star positions
star_pos = [(randint(20, WINDOW_WIDTH-20), randint(20, WINDOW_HEIGHT)) for i in range(20)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # the background
    display_surf.fill("cornsilk")
    x += 0.05

    # put stars randomly everywhere
    for pos in star_pos:
        display_surf.blit(star_surf, pos)

    player_rect.left += 0.2
    # the space ship
    display_surf.blit(player_surf, player_rect)
    pygame.display.update()


pygame.quit()