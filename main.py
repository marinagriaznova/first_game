import random

import pygame


class Ball():
    def __init__(self, pos, color):
        self.pos = pos  # (100, 100)
        self.color = color
        self.x = random.randint(-10, 10)
        self.y = random.randint(-10, 10)
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)

    def hmove(self):
        self.pos[0] += self.x
        self.pos[1] += self.y
        if self.pos[0] >= 550 or self.pos[0] <= 50:
            self.x *= -1
            self.pos[0] += self.x
        if self.pos[1] >= 250 or self.pos[1] <= 50:
            self.y *= -1
            self.pos[1] += self.y

    def renew(self):
        x, y = self.pos
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)


pygame.init()
FPS = 20

screen = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()

screen.fill((255, 255, 255))
x, y = 300, 150

count = 0
f = False
st = False
running = True
ball_list = []
first_ball = Ball([100, 100], (255, 0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                count += 1
                if count == 1 or count % 2 == 1:
                    st = True
                else:
                    st = False
            if event.button == 3:
                x1, y1 = event.pos
                ball_list.append(Ball([x1, y1], (255, 0, 0)))
    screen.fill((255, 255, 255))
    if not st:
        for i in ball_list:
            i.renew()
            i.hmove()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
