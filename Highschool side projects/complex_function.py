import pygame
import cmath
import math
from PIL import Image

d_w = 500
d_h = 500

scale = 250

pygame.init()
screen = pygame.display.set_mode((d_w,d_h))
pixAr = pygame.PixelArray(screen)

spr = []

im = Image.open("lazyspread.png")
for x in range(im.size[0]):
    spr.append(im.getpixel((x,0)))

def spread(n):
    return spr[n]

def sigmoid(x):
    return 1/(1+cmath.e**(-x/100)) 

def f(s):
    #edit this function to see change the pic
    if s == 0:
        return 0
    else:
        return cmath.exp(1/s)
        

#backg = Image.new("RGB",(d_w,d_h),(0,0,0))

for x in range(d_w):
    for y in range(d_h):
        num = f((x/scale-d_w/(2*scale))+((y/scale-d_h/(2*scale))*1j))
        col = int(  255*cmath.phase( num )/(2*cmath.pi)%255 )
        r = int(spread(col)[0] * sigmoid((num.real)**2 + (num.imag)**2) ) 
        g = int(spread(col)[1] * sigmoid((num.real)**2 + (num.imag)**2) )
        b = int(spread(col)[2] * sigmoid((num.real)**2 + (num.imag)**2) )
        pixAr[x][y] = (r,g,b)
        #backg.putpixel((x,y),(r,g,b))

#backg.save("backg.png")

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
