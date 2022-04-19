import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split()) # h: x, w: y
_map = [list(map(int, input().split())) for _ in range(h)]

hdx, hdy = [-2, -2, -1, 1, 2, 2, 1, -1], [-1, 1, 2, 2, 1, -1, -2, -2]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
min_value = w * h + 1

def bfs():
  global min_value
  
  q = deque()
  q.append([0, 0, k, 0])
  
  while q:
    cx, cy, ck, cl = q.popleft()
    if cx == (h - 1) and cy == (w - 1):
      min_value = min(min_value, cl)
      continue
    if 0 < ck:
      for i in range(8):
        nx, ny = cx + hdx[i], cy + hdy[i]
        if 0 <= nx < h and 0 <= ny < w:
          if _map[nx][ny] == 0 and cl < min_value:
              q.append([nx, ny, ck - 1, cl + 1])
    for i in range(4):
      nx, ny = cx + dx[i], cy + dy[i]
      if 0 <= nx < h and 0 <= ny < w:
        if _map[nx][ny] == 0 and cl < min_value:
            q.append([nx, ny, ck, cl + 1])

def solution():
  
  bfs()
  if min_value == (w * h + 1):
    print(-1)
  else:
    print(min_value)
  
solution()