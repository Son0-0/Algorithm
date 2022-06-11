import sys
import heapq
from collections import deque

input = sys.stdin.readline

csize = int(input())
rsize = int(input())

graph = [[] for _ in range(csize + 1)]
graph_for_bt = [[] for _ in range(csize + 1)]
indegree = [0 for _ in range(csize + 1)]
clist = [0 for _ in range(csize + 1)]

for _ in range(rsize):
    s, d, c = map(int, input().split())
    graph[s].append((d, c))
    graph_for_bt[d].append((s, c))
    indegree[d] += 1

start, destination = map(int, input().split())


def topology_sort():
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cur_cost, cur_city = heapq.heappop(queue)
        for ct, cst in graph[cur_city]:
            cost = -cur_cost + cst
            if clist[ct] < cost:
                clist[ct] = cost
            indegree[ct] -= 1
            if indegree[ct] == 0:
                heapq.heappush(queue, (-clist[ct], ct))

    return clist[-1]


def bfs():
    queue = deque()
    queue.append((0, destination))
    result = []

    while queue:
        cost, city = queue.popleft()

        for ncity, ncost in graph_for_bt[city]:
            if clist[city] == ncost + clist[ncity]:
                if not (ncity, city) in result:
                    result.append((ncity, city))
                    queue.append((cost + ncost, ncity))

    return len(result)


def solution():
    print(topology_sort())
    print(bfs())


solution()