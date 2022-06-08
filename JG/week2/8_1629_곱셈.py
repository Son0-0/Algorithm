import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())

def recur(a, b):
  if b == 1:
    return a % c
  
  target = recur(a, b//2)
  
  if b % 2 == 0:
    return target * target % c
  else:
    return target * target * a % c  

print(recur(a, b))