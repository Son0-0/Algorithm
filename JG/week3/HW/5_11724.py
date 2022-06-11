import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

v_size, e_size = map(int, input().split())
visited = [0 for _ in range(v_size + 1)]
graph = [[] for _ in range(v_size + 1)]

for _ in range(e_size):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)


def dfs(v):
    for vtx in graph[v]:
        if visited[vtx] == 0:
            visited[vtx] = 1
            dfs(vtx)


def solution():
    count = 0
    for idx in range(1, v_size + 1):
        if visited[idx] == 0:
            dfs(idx)
            count += 1

    print(count)


solution()