import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [1, 0, 1], [0, 1, 1]

N, M, T = map(int, input().split())

wmap = [list(map(int, input().split())) for _ in range(N)]
tmap = [list(map(int, input().split())) for _ in range(N)]  

# 한 번 이동할 때마다 추가로 1분이 걸림
max_value = 0

def bfs():
  global max_value
  q = deque()
  q.append([0, 0, 0, T]) # x, y, job, remain_time
  
  while q:
    cx, cy, cj, ct = q.popleft()
    if cx == (N - 1) and cy == (M - 1):
      max_value = max(max_value, cj)
    ct -= 1
    for i in range(3):
      nx, ny = cx + dx[i], cy + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if 0 <= (ct - tmap[nx][ny]):
          q.append([nx, ny, cj + wmap[nx][ny], ct - tmap[nx][ny]])
          q.append([nx, ny, cj, ct])

def solution():
  bfs()
  print(max_value)
  return 0
  
solution()