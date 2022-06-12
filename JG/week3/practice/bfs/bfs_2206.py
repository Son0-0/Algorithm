import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
_map = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []

def bfs(x, y):
  queue = deque()
  queue.append((1, x, y, 0))
  visited[x][y] = 2
  
  while queue:
    cc, cx, cy, w = queue.popleft()
    if cx == N - 1 and cy == M - 1:
      return cc
    for i in range(4):
      nx, ny = cx + dx[i], cy + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if w == 0:
          if _map[nx][ny] == 0:
            if visited[nx][ny] != 2:
              visited[nx][ny] = 2
              queue.append((cc + 1, nx, ny, w))
          else:
            queue.append((cc + 1, nx, ny, w + 1))
        else:
          if _map[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] += 1
            queue.append((cc + 1, nx, ny, w))

  return -1

def solution():
  print(bfs(0, 0))
  
solution()