from random import *
pr = 5
n = 10**(pr + 1)


mxx, mnx = 1, -1
mxy,mny = 1, -1
k = 0
for i in range(100):    
    for _ in range(int(n/100)):
        x, y = uniform(mnx,mxx), uniform(mny, mxy)
        if x**2 + y**2 <= 1:
            k += 1
    print('{0}%'.format(i+1))
print('*' * 16)
print((k/n) * 4)