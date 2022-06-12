import sys
from collections import deque

input = sys.stdin.readline
END = 100001
N, K = map(int, input().split())
move = [1, -1]
_map = [0 for _ in range(END)] # 0 ~ 17 map

def bfs(v):
  _map[v] = 1
  queue = deque()
  queue.append((v, 0))
  
  while queue:
    cur, cnt = queue.popleft()
    if cur == K:
      return cnt
    for i in range(3):
      if i == 2:
        pos = cur * 2
      else:
        pos = cur + move[i]
      
      if 0 <= pos < END and _map[pos] == 0:
        _map[pos] = 1
        queue.append((pos, cnt + 1))
  
def solution():
  print(bfs(N))

solution()