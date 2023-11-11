from random import *
import turtle as t

t.screensize(750, 750)
t.hideturtle()
t.pencolor('red')
t.pensize(5)
t.setheading(90)
t.speed(100)
fov = 60

def go(n):
    while n > 0:
        t.pendown()
        t.forward(10)
        # if t.pos()[0] == 375 and t.pos()[1] == 375:
        #     t.right(180)
        t.penup()
        t.forward(10)
        # if t.pos()[0] == 375 and t.pos()[1] == 375:
        #     t.right(180)
        n -= 20

for _ in range(150):
    angle = randrange(-fov, fov+1)
    if angle < 0:
        angle = 360 + angle
    t.right(angle)
    go(randrange(30, 91))