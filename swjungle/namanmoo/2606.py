import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []


def dfs(cur):
    for node in graph[cur]:
        if node not in visited:
            visited.append(node)
            dfs(node)


def solution():
    dfs(1)
    print(len(visited) - 1)
    return 0


solution()