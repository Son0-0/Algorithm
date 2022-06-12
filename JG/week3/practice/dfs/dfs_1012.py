import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  _map[x][y] = -1
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < N and 0 <= ny < M:
      if _map[nx][ny] == 1:
        dfs(nx, ny)


for _ in range(int(input())):
  M, N, K = map(int, input().split())
  _map = [[0] * M for _ in range(N)]

  for _ in range(K):
    x, y = map(int, input().split())
    _map[y][x] = 1
    
  cnt = 0 

  for row in range(N):
    for col in range(M):
      if _map[row][col] == 1:
        dfs(row, col)
        cnt += 1
        
  print(cnt)