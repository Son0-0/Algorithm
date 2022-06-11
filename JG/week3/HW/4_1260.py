import sys
from collections import deque

input = sys.stdin.readline

# 정점의 개수: N
# 간선의 개수: M
# 탐색을 시작할 정점의 번호: V

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
  node, target = map(int, input().split())
  graph[node].append(target)
  graph[target].append(node)
  
def dfs(start, visited = []):
  visited.append(start)
  
  for node in sorted(graph[start]):
    if not node in visited:
      visited = dfs(node, visited)
  
  return visited

def bfs(start, visited=[]):
  visited = [start]
  queue = deque()
  queue.append(start)
  
  while queue:
    v = queue.popleft()
    for node in sorted(graph[v]):
      if not node in visited:
        visited.append(node)
        queue.append(node)
        
  return visited
  
print(*dfs(V))
print(*bfs(V))