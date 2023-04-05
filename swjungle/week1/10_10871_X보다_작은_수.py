import sys

N, x = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))

for num in A:
  if num < x:
    print(num, end=" ")