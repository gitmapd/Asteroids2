from Vector import Vector
from Asteroid import Asteroid
from Vector3D import Vector3D
import random
import pygame, sys

def draw_asteroid(screen,color,bunchaster):
    for i in bunchaster:
        pygame.draw.circle(screen,color,(i.pos.x,i.pos.y),100)
pygame.init()

clock = pygame.time.Clock()

screensize = Vector(800,600)

red = (200,0,0)

a=Vector3D(1,2,3)
b=Vector3D(screensize.x//2,screensize.y//2,2)
vel=Vector3D(4,4,4)
bunchaster=[Asteroid(b,vel*random.random(),random.random()) for i in range(10)]

screen = pygame.display.set_mode((screensize.x,screensize.y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    draw_asteroid(screen,red,bunchaster)
    pygame.display.flip()
    clock.tick(60)




