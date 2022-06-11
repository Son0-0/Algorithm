import sys, heapq

input = sys.stdin.readline

n = int(input())
ans = [0] * (n + 1)
degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

def topology_sort():
    q = []
    for i in range(1, n + 1):
        if degree[i] == 0:
            heapq.heappush(q, -i)

    N = n
    while q:
        now = -heapq.heappop(q)
        ans[now] = N

        for k in graph[now]:
            degree[k] -= 1
            if degree[k] == 0:
                heapq.heappush(q, -k)

        N -= 1

def solution():
  for _ in range(1, n + 1):
      tmp = [0] + list(map(int, input().rstrip()))
      for i in range(1, n + 1):
          if tmp[i] == 1:
              graph[i].append(_)
              degree[_] += 1
  topology_sort()
  if ans.count(0) > 1:
      print(-1)
  else:
      print(*ans[1:])
      
solution()