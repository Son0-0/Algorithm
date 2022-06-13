import sys

input = sys.stdin.readline

N = int(input())
_map = [list(map(int, input().split())) for _ in range(N)]


def solution():

    odr_list = []

    for route in range(N):
        for row in range(N):
            for col in range(N):
                if _map[row][route] and _map[route][col]:
                    _map[row][col] = 1

    for m in _map:
        print(*m)


solution()