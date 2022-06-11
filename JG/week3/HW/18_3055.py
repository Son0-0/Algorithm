import sys, heapq
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
_map = [[area for area in list(map(str, input().strip()))] for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
wvisited = [[0 for _ in range(C)] for _ in range(R)]
wqueue = deque()
queue = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def water():
  for _ in range(len(wqueue)):
    wx, wy = wqueue.popleft()
    for i in range(4):
      nwx, nwy = wx + dx[i], wy + dy[i]
      if 0 <= nwx < R and 0 <= nwy < C:
        if wvisited[nwx][nwy] == 0 and _map[nwx][nwy] == ".":
          wvisited[nwx][nwy] = 1
          _map[nwx][nwy] = "*"
          wqueue.append((nwx, nwy))
          
def bfs():  
  while queue:
    water()
    for _ in range(len(queue)):
      day, x, y = heapq.heappop(queue)
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
          if visited[nx][ny] == 0 and _map[nx][ny] == ".":
            visited[nx][ny] = 1
            heapq.heappush(queue, (day + 1, nx, ny))
          if _map[nx][ny] == "D":
            return day

def solution():
  for row in range(R):
    for col in range(C):
      if _map[row][col] == "*":
        wvisited[row][col] = 1
        wqueue.append((row, col))
      if _map[row][col] == "S":
        _map[row][col] = '.'
        visited[row][col] = 1
        heapq.heappush(queue, (1, row, col))
  
  result = bfs()
  if result:
    print(result)
  else:
    print("KAKTUS")
  
solution()