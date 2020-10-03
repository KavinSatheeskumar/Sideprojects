import pygame
import math
#from PIL import Image

scale = 20
n = 10

def orbital_thing(x,y):
    x = (dw/2 - x)/scale
    y = (dh/2 - y)/scale
    r = (x**2+ y**2) ** (0.5)
    the = math.atan2(y,x) + math.pi

    output = 0

    for i in range(n):
        output += math.sin( r * (the + 2*math.pi*i))

    output = output/n

    return(output)

def col(c):
    if c >= 0:
        temp = math.atan(c)
        temp = temp * 255
        temp = int(temp)
        return (temp,0,0)
    else:
        temp = math.atan(-c)
        temp = temp*255
        temp = int(temp)
        return(0,0,temp)
    

dw = 900
dh = 600

screen = pygame.display.set_mode((dw,dh))

pixAr = pygame.PixelArray(screen)

#backg = Image.new("RGB",(dw,dh),(0,0,0))

for x in range(dw):
    for y in range(dh):
        pixAr[x][y] = col(orbital_thing(x,dh - y))
        #backg.putpixel((x,y),col(orbital_thing(x,dh - y)))

#backg.save("pfp3.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

