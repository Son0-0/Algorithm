import sys

input = sys.stdin.readline

k, n = map(int, input().split())
llist = [int(input()) for _ in range(k)]

def calc(target):
  if target == 0:
    return 0
  
  sum = 0
  for line in llist:
    sum += line // target
  return sum

def solution():
  left, right = 1, max(llist)
  
  while left <= right:
    mid = (left + right) // 2
    
    if n <= calc(mid):
      left = mid + 1
    else:
      right = mid - 1
      
  print(right)

solution()