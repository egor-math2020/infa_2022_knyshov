import pygame
from pygame.draw import *
from random import randint
pygame.init()
b = 900
a = 1200
FPS = 60
screen = pygame.display.set_mode((a, b))


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
font = pygame.font.Font("C:/Users/User/Desktop/infa_2022_knyshov/lab8/ttf.ttf", 24)
ballx = []
bally = []
ballr = []
remcol = []
ballspeedx = []
ballspeedy = []
scope = 0
dt = 2
variable = 0


# Задаем функцию - генератор шаров
def render(x, y, r, color):
    for k in range(len(x)):
        circle(screen, color[k], (x[k], y[k]), r[k])


# Задаем функцию, отвечающую за движение шаров
def move(vx, vy, x, y, r,):
    for h in range(len(x)):
        if (a-x[h]) < r[h]:
            x[h] = a-r[h]
            vx[h] = -vx[h]
            x[h] += vx[h]*dt
        if (b-y[h]) < r[h]:
            vy[h] = -vy[h]
            y[h] += vy[h]*dt
            y[h] = b-r[h]
        if y[h] < r[h]:
            vy[h] = -vy[h]
            y[h] += vy[h] * dt
            y[h] = r[h]
        if x[h] < r[h]:
            vx[h] = -vx[h]
            x[h] += vx[h] * dt
            x[h] = r[h]
        else:
            x[h] += vx[h]*dt
            y[h] += vy[h]*dt


# Задаем функцию - генератор значений
def remember():
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    ballx.append(x)
    bally.append(y)
    ballr.append(r)
    remcol.append(color)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    ballspeedx.append(vx)
    ballspeedy.append(vy)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

wait_time = 4
frame_counter = 0
while not finished:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    if frame_counter % (FPS * wait_time) == 0:
        if len(bally) <= 15:
            remember()
        render(ballx, bally, ballr, remcol)
    render(ballx, bally, ballr, remcol)
    move(ballspeedx, ballspeedy, ballx, bally, ballr)
    text = font.render("Score: " + str(scope), True, BLUE)

    screen.blit(text, [1000, 1])

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(ballx)):
                if (ballx[i] - event.pos[0]) ** 2 + (bally[i] - event.pos[1]) ** 2 <= ballr[i]**2:
                    ballx.pop(i)
                    bally.pop(i)
                    ballr.pop(i)
                    remcol.pop(i)
                    ballspeedy.pop(i)
                    ballspeedx.pop(i)

                    scope += 1
                    print('Click!')

                    break

    frame_counter += 1
print(scope)
pygame.quit()





if self.x <= self.r:
    self.vx *= (-1) * U
    self.vy *= U
    self.x = self.r
elif self.x + self.r >= WIDTH:
    self.vx *= (-1) * U
    self.vy *= U
    self.x = WIDTH - self.r
if self.y <= self.r:
    self.vy *= (-1) * U
    self.vx *= U
    self.y = self.r
elif self.y + self.r >= HEIGHT:
    self.vy *= (-1) * U
    self.vx *= U
    self.y = HEIGHT - self.r
