import pygame as pg
import time
import random

pg.init()
clock = pg.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)
gray = (115, 118, 0)
blue = (0, 0, 255)

font = pg.font.SysFont("consolas", 24)

bg = pg.display.set_mode((500, 700))

notGameOver = True
score = 0

x = 225
y = 550
move_x = "NOMOVE"

enemy_cars = []

while notGameOver:
    bg.fill(gray)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                move_x = "LEFT"
            if event.key == pg.K_RIGHT:
                move_x = "RIGHT"

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                move_x = "NOMOVE"

    if move_x == "LEFT" and x >= 10:
        x -= 5
    if move_x == "RIGHT" and x <= 440:
        x += 5

    # print(x)

    pg.draw.rect(bg, red, [x, y, 50, 65])

    if len(enemy_cars) < 12 and (len(enemy_cars) == 0 or enemy_cars[len(enemy_cars) - 1][1][1] > 65):
        enemy_cars.append([random.randrange(0, 255), [random.randrange(10, 440), -65, 50, 65]])

    # print(enemy_cars)

    for ec in range(len(enemy_cars)):
        if (abs(enemy_cars[ec][1][0] - x) <= 50) and (abs(enemy_cars[ec][1][1] - y) <= 65):
            notGameOver = False
            # gameOverText = font.render("GAME OVER", True, blue)
            # bg.blit(gameOverText, (250, 350))

        pg.draw.rect(bg, (enemy_cars[ec][0], enemy_cars[ec][0], enemy_cars[ec][0]), enemy_cars[ec][1])
        enemy_cars[ec][1][1] += 5

    if enemy_cars[0][1][1] == 765:
        enemy_cars.pop(0)
        score += 1

    pg.draw.rect(bg, white, [0, 0, 500, 30])
    scoreText = font.render("SCORE = {}".format(score), True, blue)
    bg.blit(scoreText, (190, 10))
    # clock.tick(60)
    time.sleep(0.01)
    pg.display.flip()
    # input()

if not notGameOver:
    gameOverText = font.render("GAME OVER", True, blue)
    bg.blit(gameOverText, (190, 338))
    pg.display.update()
    print("GAME OVER")
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

# [[90, [402, 625, 50, 65]],
# [1, [361, 555, 50, 65]],
# [228, [199, 485, 50, 65]],
# [234, [69, 415, 50, 65]],
# [6, [135, 345, 50, 65]],
# [50, [357, 275, 50, 65]],
# [75, [348, 205, 50, 65]],
# [24, [324, 135, 50, 65]],
# [249, [242, 65, 50, 65]]]
