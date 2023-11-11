from functools import reduce

def evaluate(cof, x):
    res = map( lambda elem, pows: elem * x ** pows, cof, list(range(len(cof)-1, -1, -1)) )
    return reduce(lambda x, y: x + y, res, 0)

#print(evaluate( [int(i) for i in input().split()], int(input())))
# print(evaluate([2, 4, 3], 10))
# 243
print(evaluate([10, 10, 10, 10, 10], 2))
#310