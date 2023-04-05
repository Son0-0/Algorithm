import sys
from collections import deque

input = sys.stdin.readline

END = 10**9
a, b = map(int, input().split())

def bfs():
  q = deque()
  q.append((a, 0))
  
  while q:
    cur, cnt = q.popleft()
    if cur == b:
      return cnt + 1
    if 1 <= (cur * 2) <= END:
      q.append((cur*2, cnt + 1))
    if 1 <= int(str(cur) + "1") <= END:
      q.append((int(str(cur) + "1"), cnt + 1))
  
  return -1
  
def solution():
  print(bfs())

solution()