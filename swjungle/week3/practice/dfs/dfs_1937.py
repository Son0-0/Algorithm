import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

size = int(input())
_map = [list(map(int, input().split())) for _ in range(size)]
visited = [[-1 for _ in range(size)] for _ in range(size)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  if visited[x][y] == -1:
    visited[x][y] = 0    
    
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < size and 0 <= ny < size:
        if _map[x][y] < _map[nx][ny]:
          visited[x][y] = max(visited[x][y], dfs(nx, ny))

  return visited[x][y] + 1
        
def solution():
  result = 0
  
  for row in range(size):
    for col in range(size):
      result = max(result, dfs(row, col))
      
  print(result)
  
solution()