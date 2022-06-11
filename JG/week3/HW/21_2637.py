import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
cost = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

for _ in range(M):
  x, y, k = map(int, input().split())
  graph[y].append((x, k))
  indegree[x] += 1

def topology_sort(result = []):
  queue = deque()
  
  for i in range(1, N + 1):
    if indegree[i] == 0:
      queue.append(i)
  
  while queue:
    cur = queue.popleft()
    for node, c in graph[cur]:
      if sum(cost[cur]) == 0: # 기본 부품이면 node에 그냥 추가
        cost[node][cur] += c
      else: # 기본 부품이 아닌 중간 부품이면 node에 지금 있는 수만큼 추가
        for _ in range(c):
          for i in range(1, N + 1):
            cost[node][i] += cost[cur][i]
      indegree[node] -= 1
      if indegree[node] == 0:
        queue.append(node)      

def solution():
  topology_sort()
  for idx, c in enumerate(cost[N]):
    if c != 0:
      print(idx, c)
  
solution()
  
  
  