import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
result = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
  global result
  nmap = [[num for num in mm] for mm in _map]
  
  queue = deque()
  for row in range(N):
    for col in range(M):
      if nmap[row][col] == 2:
        queue.append((row, col))
        
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if nmap[nx][ny] == 0:
          nmap[nx][ny] = 2
          queue.append((nx, ny))
  
  cnt = 0        
  for m in nmap:
    cnt += m.count(0)  
          
  result = max(result, cnt)

def wall(cnt):
  if cnt == 0:
    bfs()
    return
  
  for row in range(N):
    for col in range(M):
      if _map[row][col] == 0:
        _map[row][col] = 1
        wall(cnt - 1)
        _map[row][col] = 0

        
def solution():
  wall(3)
  print(result)
  
solution()