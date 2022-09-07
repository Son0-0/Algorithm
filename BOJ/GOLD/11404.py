import sys

input = sys.stdin.readline


def solution():

    n = int(input())
    graph = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == sys.maxsize:
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()


solution()
