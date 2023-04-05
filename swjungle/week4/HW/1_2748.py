import sys

input = sys.stdin.readline

num = [0 for _ in range(91)]
num[1] = 1
n = int(input())

def fibo(target):
  if target < 2:
    return num[target]
  
  if 0 < num[target]:
    return num[target]
  
  num[target] = fibo(target - 1) + fibo(target - 2)
  
  return num[target]

def solution():
  print(fibo(n))
  
solution()