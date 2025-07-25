import pygame
import math

pygame.init()
pygame.display.set_caption("doom")

class vec3():
    def __init__(self, x=0, y=0, z=0):
        self.e = [x, y, z]
    def x(self):    return self.e[0]
    def y(self):    return self.e[1]
    def z(self):    return self.e[2]

    def __neg__(self):  return vec3(-self.e[0], -self.e[1], -self.e[2])

    # tvoj_vektor[index]
    def __getitem__(self, i):  return self.e[i]
    def __setitem__(self, i, value):    self.e[i] = value

    def __iadd__(self, v):
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return self
    def __isub__(self, v):
        self.e[0] -= v.e[0]
        self.e[1] -= v.e[1]
        self.e[2] -= v.e[2]
    def __imul__(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self
    def __itruediv__(self, t):
        self.e[0] /= t
        self.e[1] /= t
        self.e[2] /= t
        return self
    
    def length(self):
        return math.sqrt(self.e[0]**2 + self.e[1]**2 + self.e[2]**2)

    def __add__(self, v):
        return vec3(self.e[0] + v.e[0], self.e[1] + v.e[1], self.e[2] + v.e[2])
    def __sub__(self, v):
        return vec3(self.e[0] - v.e[0], self.e[1] - v.e[1], self.e[2] - v.e[2])
    # NORMALAN MUL DA SE DODA
    def __rmul__(self, t):
        return vec3(self.e[0] * t, self.e[1] * t, self.e[2] * t)
    def __truediv__(self, t):
        return vec3(self.e[0] / t, self.e[1] / t, self.e[2] / t)
    def dot(u, v):
        return u.e[0]*v.e[0] + u.e[1]*v.e[1] + u.e[2]*v.e[2]
    def cross(u, v):
        return vec3(
            u.e[1] * v.e[2] - u.e[2] * v.e[1],
            u.e[2] * v.e[0] - u.e[0] * v.e[2],
            u.e[0] * v.e[1] - u.e[1] * v.e[0]
        )
    def unit_vector(v):
        return v / v.length()


# Window
width = 800
height = 600
fps = 60

# Player variables
x = 256
y = 256
dx = 0
dy = 0
player_height = 16
player_width = 16
player_speed = 3
player_angle = 270
sensitivity = 6

# Raytracing
orig = vec3(0, 0, 0)
dir = vec3(0, 0, 0)
viewport_height = height * 2
viewport_width = viewport_height * (width / height)
focal_length = 1
camera_center = vec3(0, 0, 0)

viewport_u = vec3(viewport_width, 0, 0)
viewport_v = vec3(0, -viewport_height, 0)

pixel_delta_u = viewport_u / width
pixel_delta_v = viewport_v / height

viewport_upper_left = camera_center - vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2
pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)



prozor = pygame.display.set_mode((width,height))



# Boje
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (100,10,100)
YELLOW = (255, 255, 0)





class Ray():
    def __init__(self, orig, dir):
        
        self.orig = orig
        self.dir = dir
        
    def origin(self, orig):
        return self.orig
    def direction(self):
        return self.dir
    def at(self, t):
        return self.orig + dir * t #skloniti


class Map():
    def __init__(self, map_width, map_height, map_unit, pos_x, pos_y):
        self.map_width = map_width
        self.map_height = map_height
        self.map_unit = map_unit
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.map = [
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        ]

    
    def drawMap(self, prozor):
        self.pos_y = 0
        for i in range(self.map_height):
            for j in range(self.map_width):
                if self.map[i][j] == 1:
                    pygame.draw.rect(prozor, BLUE, (self.pos_x, self.pos_y, self.map_unit, self.map_unit))
                self.pos_x += self.map_unit
            self.pos_y += self.map_unit
            self.pos_x = 0


    def collisions(map, dx, dy, x, y):
        pass

    


def player_movement(player_speed, player_angle):
    tasteri = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if tasteri[pygame.K_w]:
        dx = player_speed * math.sin(player_angle * math.pi/180)
        dy = player_speed * math.cos(player_angle * math.pi/180)
    if tasteri[pygame.K_s]:
        dx = player_speed * -math.sin(player_angle * math.pi/180)
        dy = player_speed * -math.cos(player_angle * math.pi/180)
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

# world_map = Map(16, 16, 32, 0, 0)

def ray_color(r):
    unit_direction = vec3.unit_vector(r.direction()) 
    a = 0.5*(unit_direction.y() + 1.0)
    color = (1 - a) * vec3(0, 1, 1) + a * vec3(1, 1, 0)
    return (int(255 * color.x()), int(255 * color.y()), int(255 * color.z()))




radi = True
while radi:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            radi = False
    prozor.fill(BLACK)
    # world_map.drawMap(prozor)
    for j in range(height):
        for i in range(width):
            pixel_center = pixel00_loc + i * pixel_delta_u + j * pixel_delta_v
            ray_direction = pixel_center - camera_center
            r = Ray(camera_center, ray_direction)
            # print((pixel_center.x()), (pixel_center.y()))
            # print(pixel_center)
            pygame.draw.circle(prozor, ray_color(r), ((pixel_center.x()), (pixel_center.y())), 1)


    dx, dy, player_angle = player_movement(player_speed, player_angle)
        
    x += dx
    y += dy

    # collisions(map, dx, dy, x, y)
    
    pygame.draw.rect(prozor, YELLOW, (x, y, player_width, player_height))
    pygame.draw.line(prozor, RED, (x + player_width/2, y + player_height/2),
                        ((math.sin(player_angle * math.pi / 180)*50 + x + player_width/2),
                        (math.cos(player_angle * math.pi / 180)*50 + y + player_height/2)), 2)
    pygame.display.update()
    pygame.time.delay(1000 // fps)


