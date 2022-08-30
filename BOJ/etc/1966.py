import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
  size, target = map(int, input().split())
  _list = [num for num in list(map(int, input().split()))]
  llist = [[idx, num] for idx, num in enumerate(_list)]
  
  llist.sort(key = lambda x:x[1])
  print(llist)
  print(max(llist, key = lambda x:x[1]))