import sys

input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []
for row, values in enumerate(sudoku):
    for col, value in enumerate(values):
        if value == 0:
            blank.append((row, col))
cnt = len(blank)


def is_valid(row, col, target):
    for i in range(9):
        if sudoku[i][col] == target:
            return False

    for i in range(9):
        if sudoku[row][i] == target:
            return False

    r, c = row // 3, col // 3
    for i in range(3 * r, 3 * (r + 1)):
        for j in range(3 * c, 3 * (c + 1)):
            if sudoku[i][j] == target:
                return False

    return True


def dfs(cur):
    if cur == cnt:
        for s in sudoku:
            print(*s)
        exit(0)

    for num in range(1, 10):
        x, y = blank[cur]
        if is_valid(x, y, num):
            sudoku[x][y] = num
            dfs(cur + 1)
            sudoku[x][y] = 0


def solution():

    dfs(0)


solution()
