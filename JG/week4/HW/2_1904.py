import sys

input = sys.stdin.readline

def solution():
  N = int(input())
  f, b = 1, 2
  result = 1 if N == 1 else 2
  
  for i in range(3, N + 1):
    result = (f + b) % 15746
    f, b = b, result
    
  print(result)
  
solution()