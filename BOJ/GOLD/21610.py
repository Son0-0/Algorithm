n, m = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
ddx, ddy = [-1, -1, 1, 1], [-1, 1, -1, 1]  # 대각선
water_copy = set()
cloud = set()
cloud.add((n - 1, 0))
cloud.add((n - 1, 1))
cloud.add((n - 2, 0))
cloud.add((n - 2, 1))

# cloud detect


def calc_cloud():
    global cloud

    temp = set()

    for i in range(n):
        for j in range(n):
            if 2 <= _map[i][j] and (i, j) not in cloud:
                _map[i][j] -= 2
                temp.add((i, j))

    cloud.clear()

    for element in temp:
        cloud.add(element)


def move_cloud(d, s):
    global water_copy

    temp = set()

    for x, y in cloud:
        if dx[d - 1] < 0:
            nx = x - (s % n)

            if nx < 0:
                nx += n

        else:
            nx = (x + (dx[d - 1] * s)) % n

        if dy[d - 1] < 0:
            ny = y - (s % n)

            if ny < 0:
                ny += n

        else:
            ny = (y + (dy[d - 1] * s)) % n

        temp.add((nx, ny))

        _map[nx][ny] += 1
        water_copy.add((nx, ny))

    cloud.clear()
    for x, y in temp:
        cloud.add((x, y))


def copy_water():
    temp = []

    while water_copy:
        x, y = water_copy.pop()
        cnt = 0
        for i in range(4):
            nx, ny = x + ddx[i], y + ddy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if 0 < _map[nx][ny]:
                    cnt += 1

        temp.append([x, y, cnt])

    while temp:
        x, y, c = temp.pop()
        _map[x][y] += c


def solution():
    for d, s in move:
        move_cloud(d, s)
        copy_water()
        calc_cloud()

    answer = 0
    for mm in _map:
        answer += sum(mm)

    print(answer)


solution()
