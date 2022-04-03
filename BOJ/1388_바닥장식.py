import sys

input = sys.stdin.readline
N, M = map(int, input().split())
visited = [[0 for _ in range(M)] for _ in range(N)]
llist = [list(map(str, input().strip())) for _ in range(N)]
cnt = 0


def dfs(row, col, cur):
    global cnt
    if 0 <= row < N and 0 <= col < M:
        if llist[row][col] != cur:
            return

        if visited[row][col] == 0:
            visited[row][col] = 1
            if cur == '-':
                return dfs(row, col + 1, llist[row][col])
            else:
                return dfs(row + 1, col, llist[row][col])


def solution():
    result = 0
    for row in range(N):
        for col in range(M):
            if visited[row][col] == 0:
                dfs(row, col, llist[row][col])
                result += 1

    print(result)


solution()