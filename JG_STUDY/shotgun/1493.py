import sys

input = sys.stdin.readline

l, w, h = map(int, input().split())
n = int(input())

#   1 , 2 , 4 , 8 ...
# [ 0 , 1 , 2 , 3]
clist = []
for _ in range(n):
  a, b = map(int, input().split())
  if a <= l and a <= w and a <= h:
    clist.append([2 ** a, b])
clist = reversed(clist)
    
def dq(big, small):
  
  # big
  if 0 < big:
    for cube in clist:
      if (cube[0] ** 3) <= big:
        big -= 
  
  # small
    

def solution():
  
  v = l * w * h
  
  dq(v, 0)

solution()