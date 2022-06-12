import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
_map = [list(map(str, input().strip())) for _ in range(M)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(vx, vy):
  visited = [[0 for _ in range(N)] for _ in range(M)]
  visited[vx][vy] = 1
  q = deque()
  q.append((vx, vy))
  
  result = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < M and 0 <= ny < N:
        if _map[nx][ny] == 'L' and visited[nx][ny] == 0:
          visited[nx][ny] = visited[x][y] + 1
          result = max(result, visited[nx][ny])
          q.append((nx, ny))
          
  return result - 1
        
def solution():
  result = -1
  
  for row in range(M):
    for col in range(N):
      if _map[row][col] == 'L':
        result = max(result, bfs(row, col))
        
  print(result)
        
solution()