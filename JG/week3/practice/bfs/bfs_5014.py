import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
ev = [u, -d]
visited = [0 for _ in range(f + 1)]
result = []

def bfs(v):
  queue = deque()
  visited[v] = 1
  queue.append((v, 0))
  
  while queue:
    cur, cnt = queue.popleft()
    if cur == g:
      return cnt
    for i in range(2):
      npos = cur + ev[i]
      if 0 < npos <= f and visited[npos] == 0:
        visited[npos] = 1
        queue.append((npos, cnt + 1))
  
  return "use the stairs"
        
def solution():
  print(bfs(s))
  
solution()