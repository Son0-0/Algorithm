import sys

input = sys.stdin.readline

size = int(input())
visited = [0 for _ in range(size + 1)]
graph = [[] for _ in range(size + 1)]

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)


def dfs(v):
    for vtx in graph[v]:
        if visited[vtx] == 0:
            visited[vtx] = 1
            dfs(vtx)


def solution():
    dfs(1)
    print(sum(visited) - 1)


solution()