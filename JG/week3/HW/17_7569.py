import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[[tomato for tomato in list(map(int, input().split()))] for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
queue = deque()
result = 0

def bfs():
  global result
  
  while queue:
    h, x, y = queue.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nh = h + dh[i]
      if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H:
        # if nh < 0 or H <= nh:
          # continue
        if box[nh][nx][ny] == 0:
          box[nh][nx][ny] = box[h][x][y] + 1
          result = max(result, box[nh][nx][ny])
          queue.append((nh, nx, ny))

def solution():
  for h in range(H):
    for row in range(N):
      for col in range(M):
        if box[h][row][col] == 1:
          queue.append((h, row, col))

  bfs()
  
  for h in range(H):
    for row in range(N):
      for col in range(M):
        if box[h][row][col] == 0:
          print(-1)
          return
        
  if result == 0:
    print(0)
  else:
    print(result - 1)

solution()