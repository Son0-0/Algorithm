import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
  v, e = map(int, input().split())
  graph[v].append(e)

def bfs(v):
  visited = [0 for _ in range(N + 1)]
  visited[v] = 1
  result = []
  
  queue = deque()
  queue.append((v, 0))
  
  while queue:
    vtx, count = queue.popleft()
    if count == K:
      result.append(vtx)
    for idx in graph[vtx]:
      if visited[idx] == 0:
        visited[idx] = 1
        queue.append((idx, count + 1))
  return result

def solution():
  result = bfs(X)
  if len(result) == 0:
    print(-1)
  else:
    result.sort()
    print(*result, sep="\n")

solution()