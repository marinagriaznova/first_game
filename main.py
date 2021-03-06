import pygame

class Ball():
    def __init__(self, pos, color):
        self.pos = pos   # (100, 100)
        self.color = color
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 100)
    def hmove(self):
        self.pos[0] += 1
    def renew(self):
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 100)


pygame.init()
FPS = 50

screen = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()

screen.fill((255, 255, 255))
x, y = 300, 150

count = 0
f = False
st = False
running = True

first_ball = Ball([100, 100], (255, 0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            count += 1
            if count == 1 or count % 2 == 1:
                st = True
            else:
                st = False
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 100)
    pygame.display.flip()
    screen.fill((255, 255, 255))
    first_ball.hmove()
    if not st:
        if x == 500:
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 100)
            x -= 1
        elif x == 100:
            f = True
        if f:
            x += 1
        else:
            x -= 1
    clock.tick(FPS)

pygame.quit()