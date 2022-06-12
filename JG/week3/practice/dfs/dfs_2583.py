import sys
from collections import deque

input = sys.stdin.readline

x, y, input_size = map(int, input().split())
axes = []
for _ in range(input_size):
  axes.append(list(map(int, input().split())))

paper = [[0 for _ in range(y)] for _ in range(x)]
for ax, ay, bx, by in axes:
  for row in range(ay, by):
    for col in range(ax, bx):
      paper[row][col] = 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(start_x, start_y):
  queue = deque()
  paper[start_x][start_y] = 1
  area = 1
  queue.append((start_x, start_y))
  
  while queue:
    ax, ay = queue.popleft()
    for i in range(4):
      nx, ny = ax + dx[i], ay + dy[i]
      if 0 <= nx < x and 0 <= ny < y:
        if paper[nx][ny] == 0:
          area += 1
          paper[nx][ny] = 1
          queue.append((nx, ny))
    
  return area

def solution():
  cnt = 0
  result = []
  
  for row in range(x):
    for col in range(y):
      if paper[row][col] == 0:
        result.append(bfs(row, col))
        cnt += 1
        
  print(cnt)
  print(*sorted(result))

solution()