import pygame
from random import randint
from os.path import join


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("banana🍌")
running = True
clock = pygame.time.Clock()

# plane surface
surf = pygame.Surface((50, 50))
surf.fill("red")

# importing image rocket
player_surf = pygame.image.load(join('assets', 'images', 'rocket.svg')).convert_alpha()
# rocket as an frect
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT-50))
# direction of rocket
player_dir = pygame.math.Vector2(2, -1)
# speed of rocket
player_speed = 10


# importing image star
star_surf = pygame.image.load(join('assets', 'images', 'star.svg')).convert_alpha()
# star positions
star_pos = [(randint(20, WINDOW_WIDTH-20), randint(20, WINDOW_HEIGHT)) for i in range(20)]

# importing image meteor
meteor_surf = pygame.image.load(join('assets', 'images', 'meteor.svg')).convert_alpha()
# meteor as an frect
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

# importing image laesr
laser_surf = pygame.image.load(join('assets', 'images', 'laser.svg')).convert_alpha()
# laser as an frect
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT-20))




# Game Loop
while running:
    clock.tick(30)
    print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # the background
    display_surf.fill("cornsilk")

    # put stars randomly everywhere
    for pos in star_pos:
        display_surf.blit(star_surf, pos)

    # put meteor on the centre
    display_surf.blit(meteor_surf, meteor_rect)

    
    # put laser on the left bottom
    display_surf.blit(laser_surf, laser_rect)

    # movement of player
    player_rect.center += player_dir * player_speed

    # the space ship i e the player
    display_surf.blit(player_surf, player_rect)
    pygame.display.update()


pygame.quit()