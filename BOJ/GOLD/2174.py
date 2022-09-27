import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
_map = [[0 for _ in range(a + 1)] for _ in range(b + 1)]
n, m = map(int, input().split())

robots = dict()
for idx in range(1, n + 1):
    x, y, d = map(str, input().split())
    # 로봇 초기 위치 표시
    _map[int(y)][int(x)] = idx

    # 로봇 위치 저장
    robots[idx] = [int(y), int(x), d]

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

DIR = {
    'N': 0,
    'W': 1,
    'S': 2,
    'E': 3,
    0: 'N',
    1: 'W',
    2: 'S',
    3: 'E'
}


def f_cmd(num):
    robo = robots[num]

    nx, ny = robo[0] + dx[DIR[robo[2]]], robo[1] + dy[DIR[robo[2]]]
    if 1 <= nx <= b and 1 <= ny <= a:
        if _map[nx][ny] == 0:
            _map[robo[0]][robo[1]] = 0
            _map[nx][ny] = num
            robots[num][0], robots[num][1] = nx, ny
        else:
            return False, f'Robot {num} crashes into robot {_map[nx][ny]}'
    else:
        return False, f'Robot {num} crashes into the wall'

    return True, None


def solution():
    command = deque()

    for _ in range(m):
        command.append(list(map(str, input().split())))

    while command:
        rnum, cmd, cnt = command.popleft()
        cnt = int(cnt)
        rnum = int(rnum)
        while cnt != 0:
            if cmd == 'F':
                tf, msg = f_cmd(rnum)
                if not tf:
                    print(msg)
                    return
            elif cmd == 'R':
                temp = DIR[robots[rnum][2]] - 1
                if temp < 0:
                    temp += 4
                robots[rnum][2] = DIR[temp]
            elif cmd == 'L':
                robots[rnum][2] = DIR[(DIR[robots[rnum][2]] + 1) % 4]

            cnt -= 1

    print("OK")

    return 0


solution()
