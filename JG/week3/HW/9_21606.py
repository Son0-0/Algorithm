# 실외 정점과 인접한 실내 정점들의 개수: N => N * (N - 1)
# 실내 끼리 인접한 정점: + 2

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8) # 이거 안해줘서 73점

N = int(input())  # 정점의 수
inout = list(map(int, input().strip()))  # 실내 / 실외 표시 1: 실외 0: 실내
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
result = 0

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    if inout[v1 - 1] == 1 and inout[v2 - 1] == 1:
        result += 2


def dfs(v, indoor):
    visited[v] = 1

    for idx in graph[v]:
        if inout[idx - 1] == 1:
            indoor += 1
        
        if visited[idx] == 0 and inout[idx - 1] == 0:
            indoor = dfs(idx, indoor)

    return indoor


def solution():
    global result

    for idx in range(1, N + 1):
        if visited[idx] == 0 and inout[idx - 1] == 0:
            n = dfs(idx, 0)
            result += n * (n - 1)

    print(result)


solution()