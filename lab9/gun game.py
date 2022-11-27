import math
from random import randint

import pygame


FPS = 30

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, CYAN]
U = 1/2
WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self,  x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = randint(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy

        if (WIDTH-self.x) < self.r:
            self.x = WIDTH-self.r
            self.vx = -self.vx
            self.x += self.vx
        if (HEIGHT-self.y) < self.r:
            self.vy = -self.vy
            self.y += self.vy
            self.y = HEIGHT-self.r
        if self.y < self.r:
            self.vy = -self.vy
            self.y += self.vy
            self.y = self.r
        if self.x < self.r:
            self.vx = -self.vx
            self.x += self.vx
            self.x = self.r
        else:
            self.x += self.vx
            self.y += self.vy
        self.vy -= 8 / FPS

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (((self.r + obj.r) ** 2) >=
                ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)):
            return True
        return False


class Gun:
    def __init__(self):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (30, 445, 20, 10)
        )
        x = (math.sin(self.an) * 5)
        y = (math.cos(self.an) * 5)
        lx = (math.cos(self.an) * self.f2_power)
        ly = (math.sin(self.an) * self.f2_power)
        pygame.draw.polygon(self.screen, self.color,
                            [[40 + x, 450 - y],
                             [40 + lx + x, 450 + ly - y], [40 + lx - x, 450 + ly + y], [40 - x, 450 + y]])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        """ Call functions when object is created. """
        self.screen = screen
        self.r = randint(2, 50)
        self.color = RED
        self.points = 0
        self.live = 1
        self.d = randint(35, 60)
        self.w = randint(1, 10)
        self.phi = 0
        self.x0 = randint(600, 780)
        self.y0 = randint(300, 550)
        self.x = self.x0
        self.y = self.y0

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
        self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun()
target = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end()
