import pygame
from PIL import Image
import time
import random

w = 800
h = 600

pygame.init()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("terria")
clock = pygame.time.Clock()

point = pygame.image.load("pointer.png")

air = Image.open("back 1.png")
dirt = Image.open("back 2.png")
grass = Image.open("back 3.png")
rock = Image.open("back 4.png")
tree = Image.open("back 5.png")
leaf = Image.open("back 6.png")

block_list = [air,dirt,grass,rock,tree,leaf]

block_map = []

m = random.randint(20,(int(h/10) - 20))
r = random.randint(5,10)

for d in range(int(w/10)):
    holder = []
    for e in range(int(h/10)):
        if e < m:
            holder.append(0)
        if e == m:
            holder.append(2)
        if e > m and e < m + r:
            holder.append(1)
        if e >= m + r:
            holder.append(3)

    if m == 20:
        m += 1
    elif m == (int(h/10) - 20):
        m -= 1
    else:
        q = random.randint(-2,2)
        if q == 1 or q == -1:
            q = 0
        if q == 2 or q == -2:
            q = q/2
        m += q
    if r == 0:
        r += 1
    else:
        k = random.randint(-1,1)
        r += k

    block_map.append(holder)

change_c = 0

for t in range(int(w/10)):
    for i in range(int(h/10)):
        if change_c == 0:
            c = random.randint(0,8)
        if block_map[t][i] == 2 and c == 8 and t < int(h/10)-5 and t > 5:
            block_map[t][i - 1] = 4
            block_map[t][i - 2] = 4
            block_map[t][i - 3] = 4
            block_map[t][i - 4] = 4
            block_map[t][i - 5] = 5
            block_map[t][i - 6] = 5
            block_map[t - 1][i - 5] = 5
            block_map[t + 1][i -5] = 5
            block_map[t - 2][i - 5] = 5
            block_map[t + 2][i - 5] = 5
            block_map[t - 1][i - 6] = 5
            block_map[t + 1][i - 6] = 5
            change_c = 5
            c = 7
    else:
        change_c -= 1
    if change_c < 0:
        change_c = 0

gamemode = 0

background = Image.new("RGB",(w,h),(255,255,255))

def backdate(l = None,u = None):
    global f_background
    if l == None or u == None:
        for x in range(int(w/10)):
            for y in range(int(h/10)):
                n = block_map[x][y]
                s = x * 10
                g = y * 10
                for q in range(10):
                    for p in range(10):
                        background.putpixel(((s + q),(g + p)),((block_list[n]).getpixel((q,p))))
       
    else:
        n = block_map[l][u]
        for q in range(10):
            for p in range(10):
                background.putpixel(((l * 10 + q),(u * 10 + p)),((block_list[n]).getpixel((q,p))))


    background.save("background.png")
    f_background = pygame.image.load("background.png")
    
backdate()

def text_objs(text, font, color):
    textsurface = font.render(text, True, color)
    return textsurface , textsurface.get_rect()

def write(text,x,y,wi,hi,fontz,s,color):
    Texts = pygame.font.Font(fontz,s)
    textsuf, textrect = text_objs(text,Texts,color)
    textrect.center = ((x,y))
    screen.blit(textsuf,textrect)

    pygame.display.update()

def gameloop():

    screen.blit(f_background,(0,0))
    invtory = [0,0,0,0,0]

    while True:
        instring = ""
        for c in invtory:
            if c == 0:
                instring += "|" + " "
            else:
                instring += "|" + str(c)
        instring += "|"

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        x = int(mouse[0]/10)
        y = int(mouse[1]/10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if block_map[x][y] == 0:
                        pass
                    else:
                        invtory[block_map[x][y]-1] += 1
                    block_map[x][y]=0
                if event.key == pygame.K_1:
                    if invtory[0] > 0 and block_map[x][y] == 0:
                        invtory[0] -= 1
                        block_map[x][y]=1
                if event.key == pygame.K_2:
                    if invtory[1] > 0 and block_map[x][y] == 0:
                        invtory[1] -= 1
                        block_map[x][y]=2
                if event.key == pygame.K_3:
                    if invtory[2] > 0 and block_map[x][y] == 0:
                        invtory[2] -= 1
                        block_map[x][y]=3
                if event.key == pygame.K_4:
                    if invtory[3] > 0 and block_map[x][y] == 0:
                        invtory[3] -= 1
                        block_map[x][y]=4
                if event.key == pygame.K_5:
                    if invtory[4] > 0 and block_map[x][y] == 0:
                        invtory[4] -= 1
                        block_map[x][y]=5

                backdate(x,y)
        pygame.display.flip()

        screen.blit(f_background,(0,0))
        write(instring,50,20,40,20,"freesansbold.ttf",10,(0,0,0))
        screen.blit(point,(x*10,y*10))

        
gameloop()
