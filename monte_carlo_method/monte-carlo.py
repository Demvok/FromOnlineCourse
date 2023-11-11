from random import *
from turtle import turtle as t

n = 10**6
mxx, mnx = 2, -2
mxy,mny = 2, -2

k = 0
for _ in range(n):
    x, y = uniform(mnx,mxx), uniform(mny, mxy)
    if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
        k += 1

