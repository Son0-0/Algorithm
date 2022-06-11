# import sys, heapq
# # from collections import deque

# input = sys.stdin.readline

# size = int(input())
# graph = [[] for _ in range(size + 1)]
# indegree = [0 for _ in range(size + 1)]
# glist = [0 for _ in range(size + 1)]

# for idx in range(size):
#   graph[idx + 1].append(0)
#   for i, num in enumerate(map(int, input().strip())):
#     graph[idx + 1].append(num)
#     if num == 1:
#       indegree[i + 1] += 1

# for g in graph:
#   print(g)

# def topology_sort():
#   cnt = 1
#   queue = []
#   temp = []

#   for idx in range(1, size + 1):
#     if indegree[idx] == 0:
#       glist[cnt] = idx
#       heapq.heappush(queue, (idx, cnt))
#       cnt += 1

#   while queue:
#     for _ in range(len(queue)):
#       cur, cnt = heapq.heappop(queue)
#       for idx in range(1, size + 1):
#         if graph[cur][idx] == 1:
#           indegree[idx] -= 1
#           if indegree[idx] == 0:
#             glist[cnt + 1] = idx
#             heapq.heappush(temp, (idx, cnt + 1))
#     for _ in range(len(temp)):
#       heapq.heappush(queue, heapq.heappop(temp))

# def solution():
#   num = [0 for _ in range(size + 1)]
#   nlist = topology_sort()
#   print("glist", glist)


# solution()

import sys
import heapq

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
