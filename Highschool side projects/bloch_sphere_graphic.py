import pygame
import math
import lin_module
from PIL import Image

def project(p,r_f):
    c = p[3]
    pn = [p[0],p[1],p[2]+c_z]
    pn = [c_z*pn[0]/pn[2] + d_w/2,c_z*pn[1]/pn[2] + d_h/2]
    
    r = int(c_z*r_f/(p[2] + c_z))
    for x in range(r):
        for y in range(r):
            pixAr[int(pn[0])+x][int(pn[1])+y] = c
            #im.putpixel((int(pn[0]+x),int(pn[1]+y)),c)

pygame.init()

d_h = 600
d_w = 800

screen = pygame.display.set_mode((d_w,d_h))
screen.fill((0,0,0))
clock = pygame.time.Clock()
pixAr = pygame.PixelArray(screen)

n = 100
r = 200

col = (255,255,255)
c_z = (d_w + d_h)/2

rx = 0.3
ry = 0.2
rz = 0.0

Z = [
    [math.cos(rz),math.sin(rz),0],
    [-math.sin(rz),math.cos(rz),0],
    [0,0,1]
    ]

Y = [
    [math.cos(ry),0,-math.sin(ry)],
    [0,1,0],
    [math.sin(ry),0,math.cos(ry)]
    ]

X = [
    [1,0,0],
    [0,math.cos(rx),math.sin(rx)],
    [0,-math.sin(rx),math.cos(rx)]
    ]

tau = 2 * math.pi

points = []

#im = Image.new("RGB", (d_w,d_h),(0,0,0))

for i in range(n):
    points.append([0,0,int(1.3*r*i/n),(255,255,255)])
    points.append([0,-int(1.3*r*i/n),0,(255,255,255)])
    points.append([0,int(1.3*r*i/n),0,(255,255,255)])
    points.append([0,0,-int(1.3*r*i/n),(255,255,255)])
    points.append([int(1.3*r*i/n),0,0,(255,255,255)])
    points.append([-int(1.3*r*i/n),0,0,(255,255,255)])
    points.append([r*math.cos(tau*i/n),r*math.sin(tau*i/n),0,(255,255,255)])
    points.append([r*math.cos(tau*i/n),0,r*math.sin(tau*i/n),(255,255,255)])
    points.append([0,r*math.cos(tau*i/n),r*math.sin(tau*i/n),(255,255,255)])

for x in points:
    x1 = x[:3]
    x1 = lin_module.matrix_mult(Y,x1)
    x1 = lin_module.matrix_mult(Z,x1)
    x1 = lin_module.matrix_mult(X,x1)
    x1.append(x[3])
    project(x1,5)
    pygame.display.update()

#im.save("bloch.png")
#im.show()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((0,0,0))
    
    Z = [
        [math.cos(rz),math.sin(rz),0],
        [-math.sin(rz),math.cos(rz),0],
        [0,0,1]
        ]

    Y = [
        [math.cos(ry),0,-math.sin(ry)],
        [0,1,0],
        [math.sin(ry),0,math.cos(ry)]
        ]

    X = [
        [1,0,0],
        [0,math.cos(rx),math.sin(rx)],
        [0,-math.sin(rx),math.cos(rx)]
        ]

    for x in points:
        x1 = x[:3]
        x1 = lin_module.matrix_mult(Y,x1)
        x1 = lin_module.matrix_mult(Z,x1)
        x1 = lin_module.matrix_mult(X,x1)
        x1.append(x[3])
        project(x1,5)

    rx += 0.01
    ry += 0.01
    rz += 0.00
    
    clock.tick(48)
    pygame.display.update()

    
