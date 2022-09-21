import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
_map = []
kraj = deque()

r, c = map(int, input().split())
cx, cy = 0, 0
for i in range(r):
    temp = list(map(str, input().strip()))
    for j, t in enumerate(temp):
        if t == 'I':
            cx, cy = i, j
        elif t == 'R':
            kraj.append([i, j])

    _map.append(temp)
op = deque(map(int, input().strip()))


def solution():
    global cx, cy, kraj

    cnt = 0

    while op:
        cnt += 1
        n = op.popleft() - 1
        nx, ny = cx + dx[n], cy + dy[n]
        if _map[nx][ny] == 'R':
            # 미친 아두이노 만나서 끝내기
            print(f'kraj {cnt}')
            return
        else:
            # 원래 종수 위치 지우기
            _map[cx][cy] = '.'
            # 현재 종수 위치 표시
            _map[nx][ny] = 'I'
            # 종수 위치 갱신
            cx, cy = nx, ny

        temp = dict()
        while kraj:
            ckx, cky = kraj.popleft()
            mval, midx = 1e9, 0
            for i in range(9):
                nkx, nky = ckx + dx[i], cky + dy[i]
                target = abs(cx - nkx) + abs(cy - nky)
                if target < mval:
                    midx = i
                    mval = target

            nkx, nky = ckx + dx[midx], cky + dy[midx]
            if _map[nkx][nky] == 'I':
                print(f'kraj {cnt}')
                return
            _map[ckx][cky] = '.'

            if (nkx, nky) in temp:
                temp[(nkx, nky)] += 1
            else:
                temp[(nkx, nky)] = 1

        for t in temp:
            if temp[t] == 1:
                kraj.append([t[0], t[1]])
                _map[t[0]][t[1]] = 'R'

    for m in _map:
        print(*m, sep='')


solution()
