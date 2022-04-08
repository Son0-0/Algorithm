import sys

t = int(sys.stdin.readline())

def recur(k, n):
  if k == 0:
    return n
  elif n == 0:
    return 0
  return recur(k, n-1) + recur(k-1, n)

for _ in range(t):
  k = int(sys.stdin.readline()) # 몇층
  n = int(sys.stdin.readline()) # 몇호
  
  if k < 15 and n < 15:
    print(recur(k, n))