import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
distance = [sys.maxsize for _ in range(n + 1)]

for _ in range(int(input())):
    s, d, c = map(int, input().split())
    graph[s].append((d, c))
src, dest = map(int, input().split())


def solution():
    q = []
    heappush(q, [0, src])

    while q:
        dis, cur = heappop(q)
        if distance[cur] < dis:
            continue
        for node in graph[cur]:
            cost = dis + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heappush(q, [cost, node[0]])

    print(distance[dest])


solution()
