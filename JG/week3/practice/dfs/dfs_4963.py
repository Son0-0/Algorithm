import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, y, mmap):
  mmap[x][y] = -1
  
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < len(mmap) and 0 <= ny < len(mmap[0]):
      if mmap[nx][ny] == 1:
        mmap[nx][ny] = -1
        dfs(nx, ny, mmap)

while True:
  w, h = map(int, input().split())
  
  if w == h and w == 0:
    break
  
  _map = [[num for num in list(map(int, input().split()))] for _ in range(h)]
  cnt = 0
  
  for row in range(h):
    for col in range(w):
      if _map[row][col] == 1:
        dfs(row, col, _map)
        cnt += 1
  
  print(cnt)
    
  