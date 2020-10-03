import math
import pygame
import cmath
from PIL import Image

def mapping(t,a):
    if (math.sin(t)-1)*(1 + math.sin(a)) == 0:
        x = 0
    else:
        x = ( ((-math.sin(t)-1)*((math.cos(a))**2))/(math.sin(t)-1) ) ** (0.5)

    if (a > math.pi/2) and (a < (3*math.pi)/2):
        x = -x
    
    y = x * math.tan(a)

    return(x,y)

def f(x,y):
    z = x + y*1j
    if z != -1:
        w = (z-1)/(z+1)
    else:
        w = 0
    return (w.real,w.imag)

pygame.init()


spr = []

im = Image.open("lazyspread.png")
for x in range(im.size[0]):
    spr.append(im.getpixel((x,0)))

dw = 300
dh = 600

screen = pygame.display.set_mode((dw,dh))
pixAr = pygame.PixelArray(screen)

#backg = Image.new("RGB",(dw,dh),(0,0,0))

for t in range(dw):
    for a in range(dh):
        t_p = (t*math.pi/dw) - math.pi/2
        a_p = a*2*math.pi/dh
        x = mapping(t_p,a_p)[0]
        y = mapping(t_p,a_p)[1]
        z = f(x,y)[0] + f(x,y)[1]*1j

        if (f(x,y)[0]%1 <= 0.1) or (f(x,y)[0]%1 >=0.9) or (f(x,y)[1]%1 <= 0.1) or (f(x,y)[1]%1 >=0.9):
            pixAr[t][-a] = (0,0,0)
            #backg.putpixel((t,dh-a-1),(0,0,0))
        else:
            col = int( (255* (cmath.phase(z))/(2*math.pi))%255 )
            pixAr[t][-a] = (spr[col][0],spr[col][1],spr[col][2])
            #backg.putpixel((t,dh-a-1),(spr[col][0],spr[col][1],spr[col][2]))

#backg.save("reimann_sphere.png")

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
