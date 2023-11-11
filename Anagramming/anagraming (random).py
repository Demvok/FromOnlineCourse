from random import *
import sys
sys.stdin = open('word.txt', 'r', encoding='UTF-8')
inp = list(input())
sys.stdin.close()

shuffle(inp)
print(''.join(inp))