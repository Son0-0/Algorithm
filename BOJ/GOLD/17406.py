import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]
rotate = []
for _ in range(k):
    r, c, s = map(int, input().split())
    rotate.append([r - 1, c - 1, s])
min_value = sys.maxsize


def dfs(copied_map, visited=[]):
    if len(visited) == k:
        global min_value
        for x in range(n):
            min_value = min(min_value, sum(copied_map[x]))
        return

    for i in range(k):
        if i not in visited:
            r, c, s = map(int, rotate[i])

            x1, y1 = r - s, c - s
            x2, y2 = r + s, c + s

            # 회전 수
            cnt = abs(x2 - x1) + 1 // 2

            # 전 상태 복사
            rotated_map = [[m for m in mm] for mm in copied_map]

            # 회전
            for c in range(cnt):
                # y - 1 part
                for ym in range(y1 + c + 1, y2 - c + 1):
                    rotated_map[x1 + c][ym] = copied_map[x1 + c][ym - 1]
                # x - 1 part
                for xm in range(x1 + c + 1, x2 - c + 1):
                    rotated_map[xm][y2 - c] = copied_map[xm - 1][y2 - c]
                # y + 1 part
                for yp in range(y2 - c - 1, y1 + c - 1, -1):
                    rotated_map[x2 - c][yp] = copied_map[x2 - c][yp + 1]
                # x + 1 part
                for xp in range(x2 - c - 1, x1 + c - 1, -1):
                    rotated_map[xp][y1 + c] = copied_map[xp + 1][y1 + c]

            dfs(rotated_map, visited + [i])


def solution():

    dfs(_map, [])
    print(min_value)

    return 0


solution()
