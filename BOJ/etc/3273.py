# 9
# 5 12 7 10 9 1 2 3 11
# 13

import sys

input = sys.stdin.readline

n = int(input())
llist = list(map(int, input().split()))
llist.sort()
x = int(input())

def solution():
  p1, p2 = 0, len(llist) - 1
  
  cnt = 0
  while p1 < p2:
    target = llist[p1] + llist[p2]
    if target == x:
      cnt += 1
      p1 += 1
      p2 -= 1
    elif target < x:
      p1 += 1
    else:
      p2 -= 1
        
  print(cnt)
  
solution()