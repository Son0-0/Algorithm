import sys
import heapq

input = sys.stdin.readline


def dijkstra(v, graph, visited, cost):
    visited[v] = True

    queue = []
    heapq.heappush(queue, (0, v))

    while queue:
        cur_cost, city = heapq.heappop(queue)
        if cost[city] < cur_cost:
            continue

        for road in graph[city]:
            ccost = cur_cost + road[1]

            if ccost < cost[road[0]]:
                cost[road[0]] = ccost
                heapq.heappush(queue, (ccost, road[0]))


def solution():
    N = int(input())  # 도시의 개수
    M = int(input())  # 버스의 개수

    graph = [[] for _ in range(N + 1)]  # 도시 -> 도시 버스 정보
    visited = [False for _ in range(N + 1)]  # 방문 리스트
    costlist = [sys.maxsize for _ in range(N + 1)]  # 비용 리스트

    for _ in range(M):
        org, dest, cost = map(int, input().split())  # 출발지, 목적지, 비용
        graph[org].append((dest, cost))

    origin, destination = map(int, input().split())  # 출발지, 목적지

    dijkstra(origin, graph, visited, costlist)
    print(costlist[destination])


solution()