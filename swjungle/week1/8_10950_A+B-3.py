import sys

size = int(sys.stdin.readline())

for i in range(0, size):
  a, b = list(map(int, sys.stdin.readline().split()))
  print(a + b)