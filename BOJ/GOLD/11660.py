import sys


input = sys.stdin.readline

n, m = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(n)]
_input = [list(map(int, input().split())) for _ in range(m)]
_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]


def solution():

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            _sum[i][j] = _sum[i][j - 1] + _sum[i - 1][j] - \
                _sum[i - 1][j - 1] + num[i - 1][j - 1]

    for x1, y1, x2, y2 in _input:
        print(_sum[x2][y2] - _sum[x1 - 1][y2] -
              _sum[x2][y1 - 1] + _sum[x1-1][y1-1])


solution()
