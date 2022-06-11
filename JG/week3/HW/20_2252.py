import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1  

def topology_sort(result = []):
  queue = deque()

  for idx in range(1, N + 1):
    if indegree[idx] == 0:
      queue.append(idx)

  while queue:
    cur = queue.popleft()
    result.append(cur)
    for idx in graph[cur]:
      indegree[idx] -= 1
      if indegree[idx] == 0:
        queue.append(idx)
  
  
  return result

def solution():
  print(*topology_sort(), end=' ')
  
solution()