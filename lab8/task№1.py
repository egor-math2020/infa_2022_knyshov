import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))
White=(245,245,245)
screen.fill(White)
color=(237,255,33)
circle(screen,color, (200, 200), 150)
circle(screen,(255,0,0),(150,150),35)
circle(screen,(255,0,0),(250,150),40)
circle(screen,(19,19,19),(150,150),15)
circle(screen,(19,19,19),(250,150),17)
polygon(screen,(19,19,19),[[100,250],[300,250],[300,280],[100,280]])
polygon(screen,(19,19,19),[[220,120],[205,100],[330,50],[350,65]])
polygon(screen,(19,19,19),[[180,122],[195,100],[70,50],[50,67]])
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

