import pygame
import math

w = 600
h = 800

running_angle = 0
position = (int(w/2),int(h/2))

tau = 6.28318530717958647692

pygame.init()
screen = pygame.display.set_mode((w,h))
pixAr = pygame.PixelArray(screen)
pygame.display.set_caption("turtle_remake")

screen.fill((255,255,255))

def forward(distance):
    global position
    pygame.draw.line(screen, (0,0,0), position, (int(position[0] + distance * math.cos(running_angle)), int(position[1] + distance * math.sin(running_angle))),1)
    position = (int(position[0] + distance * math.cos(running_angle)), int(position[1] + distance * math.sin(running_angle)))
    
def turn(angle):
    global running_angle
    running_angle -= angle

##insert code here
    
path = ["f"]
store = []

def dragon(itterations,angle,length):
    for x in range(itterations):
        store = path[:]
        path.append("l")
        store.reverse()
        for y in range(len(store)-1):
            if store[y] == "r":
                store[y] = "l"
            elif store[y] == "l":
                store[y] = "r"
        path.extend(store)
            
    for w in path:
        if w == "f":
            forward(length)
        elif w == "r":
            turn(-angle)
        elif w == "l":
            turn(angle)

dragon(10,tau/4,6)


##finish code here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
