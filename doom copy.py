import pygame
import math

pygame.init()
pygame.display.set_caption("doom")

# Window
width = 800
height = 600
fps = 60

# Map

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
viewport_height = 2
viewport_width = viewport_height * (width / height)

prozor = pygame.display.set_mode((width,height))



# Boje
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (100,10,100)
YELLOW = (255, 255, 0)

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
    
    def lenght(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __add__(self, v):
        return vec3(self.e[0] + v.e[0], self.e[1] + v.e[1], self.e[2] + v.e[2])
    def __sub__(self, v):
        return vec3(self.e[0] - v.e[0], self.e[1] - v.e[1], self.e[2] - v.e[2])
    def __rmul__(self, t):
        return vec3(self.e[0] * t, self.e[1] * t, self.e[2] * t)
    def __truediv__(self, t):
        return vec3(self.e[0] / t, self.e[1] / t, self.e[2] / t)
    def dot(self, u, v):
        return u.e[0]*v.e[0] + u.e[1]*v.e[1] + u.e[2]*v.e[2]
    def cross(self, u, v):
        return vec3(
            u.e[1] * v.e[2] - u.e[2] * v.e[1],
            u.e[2] * v.e[0] - u.e[0] * v.e[2],
            u.e[0] * v.e[1] - u.e[1] * v.e[0]
        )
    def unit_vector(self, v):
        return v / self.lenght(v)


class Ray():
    def __init__(self, orig, dir, focal_lenght, viewport_height, viewport_width, camera_center, viewport_u, viewport_v):
        self.viewport_u = viewport_u
        self.viewport_v = viewport_v
        self.focal_lenght = focal_lenght
        self.viewport_height = viewport_height
        self.viewpor_width = viewport_width
        self.camera_center = camera_center
        self.orig = orig
        self.dir = dir
        
        self.pixel_delta_u = self.viewport_u / width
        self.pixel_delta_v = self.viewport_v / height

        self.viewport_upper_left = self.camera_center- vec3(0, 0, self.focal_lenght) - self.viewport_u/2 - self.viewport_v/2
        self.pixel00_loc = self.viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)
    def origin(self, orig):
        return self.orig
    def direction(self, dir):
        return self.dir
    def at(self, t):
        return self.orig + dir * t
    def rayColor(self, r):
        return (0, 0, 0,)
    def drawRays(self):
        for i in(height):
            for j in(width):
                pass

# rays = Ray(vec3(256, 256, 0), vec3(-1, 0, 0), 1, 2, 4, vec3(0, 0, 0), vec3(width, 0, 0), vec3(0, -height, 0))  

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

def main():






    radi = True
    while radi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                radi = False
        prozor.fill(BLACK)
        # world_map.drawMap(prozor)

        tasteri = pygame.key.get_pressed()
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


if __name__ == '__main__':
    main()
    pygame.quit()

