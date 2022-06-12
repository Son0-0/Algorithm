import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

size = int(input())
graph = [[] for _ in range(size + 1)]
for _ in range(size - 1):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))
result = []
visited = [0 for _ in range(size + 1)]


def dfs(v, length):
    for vtx, vtx_len in graph[v]:
        if visited[vtx] == 0:
            visited[v] = 1
            result.append((dfs(vtx, length + vtx_len), vtx))
            visited[v] = 0

    return length


def solution():
    dfs(1, 0)
    if len(result) == 0:
      print(0)
      return
    else:
      v = sorted(result)[-1][1]
      result.clear()
      dfs(v, 0)
      print(sorted(result)[-1][0])


solution()