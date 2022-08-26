import sys

input = sys.stdin.readline

s = [list(map(int, input().split())) for _ in range(9)]
blank = []

for row in range(9):
    for col in range(9):
        if s[row][col] == 0:
            blank.append([row, col])
cnt = len(blank)


def is_valid(x, y, num):
    # check if row valid
    for i in range(9):
        if num == s[x][i]:
            return False

    # check if col valid
    for i in range(9):
        if num == s[i][y]:
            return False

    # check 3 * 3 area is valid
    row, col = x // 3, y // 3
    for i in range(3 * row, 3 * (row + 1)):
        for j in range(3 * col, 3 * (col + 1)):
            if s[i][j] == num:
                return False

    return True


def dfs(cur):
    if cur == cnt:
        for num in s:
            print(*num)
        exit(0)

    for i in range(1, 10):
        x, y = blank[cur]
        if is_valid(x, y, i):
            s[x][y] = i
            dfs(cur + 1)
            s[x][y] = 0


def solution():
    dfs(0)


solution()
