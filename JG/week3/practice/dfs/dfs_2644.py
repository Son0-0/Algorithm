import sys

input = sys.stdin.readline

nsize = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(nsize + 1)]
visited = [0 for _ in range(nsize + 1)]
result = []

for _ in range(int(input())):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
  
def dfs(start, cnt):
  cnt += 1
  visited[start] = 1
  
  if start == b:
    result.append(cnt)
  
  for idx in graph[start]:
    if visited[idx] == 0:
      dfs(idx, cnt)

  return 0
  
def solution():
  dfs(a, 0)
  if len(result) == 0:
    print(-1)
  else:
    print(result[0] - 1)
        
solution()