import pygame
import math

pygame.init()
pygame.display.set_caption("doom")

# Window
width = 1024
height = 512
fps = 60

#Map
map_width = 16
map_height = 16
map_unit = 32

prozor = pygame.display.set_mode((width,height))
# Player variables
x = 512
y = 256
dx = 0
dy = 0
player_height = 16
player_width = 16
player_speed = 3
player_angle = 180
sensitivity = 6

#Boje
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (100,10,100)
YELLOW = (255, 255, 0)
 
def map(map_width, map_height, map_unit):
    pos_x = 0
    pos_y = 0
    map = [
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    ]

    for i in range(map_height):
        for j in range(map_width):
            if map[i][j] == 1:
                pygame.draw.rect(prozor, BLUE, (pos_x, pos_y, map_unit, map_unit))
            pos_x += map_unit
        pos_y += map_unit
        pos_x = 0


def player_movement(player_speed, player_angle):
    dx = 0
    dy = 0
    if tasteri[pygame.K_w]:
        dx = player_speed * math.sin(player_angle * math.pi/180)
        dy = player_speed * math.cos(player_angle * math.pi/180)
    if tasteri[pygame.K_s]:
        dx = player_speed * -math.sin(player_angle * math.pi/180)
        dy = player_speed * -math.cos(player_angle * math.pi/180)
        player_angle += sensitivity
        if player_angle >= 360:
            player_angle = 0
    if tasteri[pygame.K_d]:
        dy = player_speed * math.sin(player_angle * math.pi/180)
        dx = player_speed * -math.cos(player_angle * math.pi/180)
        
    if tasteri[pygame.K_a]:
        dy = player_speed * -math.sin(player_angle * math.pi/180)
        dx = player_speed * math.cos(player_angle * math.pi/180)
    if tasteri[pygame.K_RIGHT]:
        player_angle -= sensitivity
        if player_angle < 0:
            player_angle = 360
    if tasteri[pygame.K_LEFT]:
        player_angle += sensitivity
        if player_angle > 360:
            player_angle = 0
            
    return dx, dy, player_angle




radi = True
while radi:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            radi = False
    
    prozor.fill(BLACK)
    map(map_width, map_height, map_unit)

    tasteri = pygame.key.get_pressed()
    dx, dy, player_angle = player_movement(player_speed, player_angle)
        
    x += dx
    y += dy

    
    pygame.draw.rect(prozor, YELLOW, (x, y, player_width, player_height))
    pygame.draw.line(prozor, RED, (x + player_width/2, y + player_height/2),
                      ((math.sin(player_angle * math.pi / 180)*50 + x + player_width/2),
                        (math.cos(player_angle * math.pi / 180)*50 + y + player_height/2)), 2)
    pygame.display.update()
    pygame.time.delay(1000 // fps)

pygame.quit()