import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

result = 0
def bfs():
  global result  
  
  while queue:
    cur_x, cur_y = queue.popleft()
    for i in range(4):
      nx, ny = cur_x + dx[i], cur_y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if box[nx][ny] == 0:
          box[nx][ny] = box[cur_x][cur_y] + 1
          result = max(result, box[nx][ny])
          queue.append((nx, ny))
        
def solution():
  for row in range(N):
    for col in range(M):
      if box[row][col] == 1:
        queue.append((row, col))
  bfs()

  for row in range(N):
    for col in range(M):
      if box[row][col] == 0:
        print(-1)
        return
  
  if result == 0:
    print(0)
  else:
    print(result - 1)
  
solution()