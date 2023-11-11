from random import *
import turtle as t

def func(x, y):
    #return x**2 + y**2 <= 1
    return -x - y//4 > -1 and x**2 - y < 0

t.Screen().setup(1000, 1000)
t.pensize(10)
t.speed(1000000)
t.hideturtle()
t.penup()

n = 10**6
mxx, mnx = 1, -1
mxy,mny = 1, -1

for _ in range(n):
    x, y = uniform(mnx,mxx), uniform(mny, mxy)
    t.goto(int(x*500), int(y*500))
    t.pendown()
    if  func(x, y):
        t.pencolor('red')
    else:
        t.pencolor('gray')
    #t.pensize(10)
    t.dot()
    t.penup()

