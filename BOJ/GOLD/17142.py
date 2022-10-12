# 7 3
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 2 0 1 1
# 0 1 0 0 0 0 0
# 2 1 0 0 0 0 2
answer = 1e9
n, m = map(int, input().split())
_map = []
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
virus = []
zero_set = set()

for i in range(n):
    _map.append(list(map(int, input().split())))
    for j, c in enumerate(_map[i]):
        if c == 0:
            zero_set.add((i, j))
        elif c == 2:
            virus.append((i, j))


def simulate(visited):
    vset = set()
    zset = set(z for z in zero_set)
    dvset = set()

    # 활성 바이러스 / 비활성 바이러스 표시
    for i in range(len(virus)):
        if i in visited:
            vset.add(virus[i])
        else:
            dvset.add(virus[i])

    time = 0
    while vset:
        length = len(vset)
        tset = set()
        for idx in range(length):
            cx, cy = vset.pop()

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if (nx, ny) in zset:
                        zset.remove((nx, ny))
                        tset.add((nx, ny))
                    elif (nx, ny) in dvset:
                        dvset.remove((nx, ny))
                        tset.add((nx, ny))

            if len(zset) == 0:
                return time + 1

        time += 1

        if len(zset) == 0:
            return time

        vset = set(t for t in tset)

    return 1e9


def dfs(cur, visited):
    global answer

    if len(visited) == m:
        answer = min(answer, simulate((visited)))
        return

    for i in range(cur + 1, len(virus)):
        dfs(i, visited + [i])


def solution():
    # virus 확인
    if len(zero_set) == 0:
        return print(0)

    for i in range(len(virus)):
        dfs(i, [i])

    if answer == 1e9:
        print(-1)
    else:
        print(answer)

solution()