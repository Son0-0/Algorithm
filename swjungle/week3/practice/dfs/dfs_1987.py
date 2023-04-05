import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
_map = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [0 for _ in range(26)]
max_value = 0

def dfs(x, y, cnt):
  global max_value, visited
  max_value = max(max_value, cnt)
  
  if max_value == 26:
    return
  
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
      if visited[ord(_map[nx][ny]) - 65] == 0:
        visited[ord(_map[nx][ny]) - 65] = 1
        dfs(nx, ny, cnt + 1)
        visited[ord(_map[nx][ny]) - 65] = 0
  
def solution():
  visited[ord(_map[0][0]) - 65] = 1
  dfs(0, 0, 1)
  print(max_value)
  
solution()