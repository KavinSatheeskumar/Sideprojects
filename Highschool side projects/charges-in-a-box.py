import pygame
import math
#from PIL import Image

def square(x,y,s,c):
    for i in range(1-s,s):
        for j in range(1-s,s):
            pixAr[x+i][y+j] = c
            #if math.floor(100*t)==200:
                #im.putpixel((x+i + 360,y+j), (int(c[0]), int(c[1]), int(c[2])))

def project(p, c):
    pn = [p[0] - d_s/2, p[1] - d_s/2, p[2] - d_s/2]
    pn = [math.cos(t) * pn[0] + math.sin(t) * pn[2], pn[1], math.cos(t) * pn[2] - math.sin(t) * pn[0] ]
    pn = [pn[0] + d_s/2, pn[1] + d_s/2, pn[2] + d_s/2]
    #square(int( (d_s/2)*(pn[0] - d_s/2)/pn[2] + d_s/2 ), int((d_s/2)*(pn[1] - d_s/2)/pn[2] + d_s/2), int((10*d_s/6)/pn[2]), c)
    pygame.draw.circle(screen, c, (int( (d_s/2)*(pn[0] - d_s/2)/pn[2] + d_s/2 ),int((d_s/2)*(pn[1] - d_s/2)/pn[2] + d_s/2)), int((10*d_s/6)/pn[2]))

print("to start the animation, press the 'up' key")

pygame.init()

t = 0

d_s = 800

screen = pygame.display.set_mode((d_s,d_s))
screen.fill((0,0,0))
clock = pygame.time.Clock()
pixAr = pygame.PixelArray(screen)

n1 = 30
n2 = 15
d = []
t1 = []
t2 = []
v = []
a = []

#im = Image.new("RGB", (2160,1440), (0,0,0))

for i in range(n1):
    for j in range(n2):
        k = n2*i + j
        d.append([d_s/2,d_s/2,d_s/2])
        t1.append( 2*math.pi * i/n1 )
        t2.append( math.pi * j/n2 )
        v.append([800 * 0.25 * math.cos(t1[k]) * math.sin(t2[k]),
                  800 * 0.25 * math.sin(t1[k]) * math.sin(t2[k]),
                  800 * 0.25 * math.cos(t2[k])
                 ])
        a.append([0,0,0])

dt = 0.01

go = False
while True:

    if go:
        screen.fill((0,0,0))
        for i in range(n1):
            for j in range(n2):
                k = n2*i + j

                a[k][0] = 10000000/(d[k][0]**2) - 10000000/((d_s-d[k][0])**2)
                a[k][1] = 10000000/(d[k][1]**2) - 10000000/((d_s-d[k][1])**2)
                a[k][2] = 10000000/(d[k][2]**2) - 10000000/((d_s-d[k][2])**2)
                v[k][0] += a[k][0] * dt
                v[k][1] += a[k][1] * dt
                v[k][2] += a[k][2] * dt
                d[k][0] += v[k][0] * dt
                d[k][1] += v[k][1] * dt
                d[k][2] += v[k][2] * dt

                project( d[k], (255 * int(d[k][0])/d_s, 255 * int(d[k][1])/d_s, 255 * int(d[k][2])/d_s) )
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                go = True
                print("This is a simulation of of a number of 'electrons',")
                print("bound inside of a negatively charged box.")
                print("In order to make the animation play faster, (and because it looks nicer),")
                print("The electron's effect on each other is ignored.")

    pygame.display.update()
    #if math.floor(100*t) == 200:
    #    im.save("coolball.png")
    #    im.show()
    t += dt
    clock.tick(48)
