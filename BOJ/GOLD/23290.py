m, s = map(int, input().split())
fish, copied_fish, smell = dict(), dict(), dict()
for _ in range(m):
    x, y, d = map(int, input().split())
    if (x, y) in fish:
        if (d - 1) in fish[(x, y)]:
            fish[(x, y)][d - 1] += 1
        else:
            fish[(x, y)][d - 1] = 1
    else:
        fish[(x, y)] = {(d - 1): 1}
sx, sy = map(int, input().split())

dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
sdx, sdy = [-1, 0, 1, 0], [0, -1, 0, 1]


def copy_fish():
    for key in fish:
        copied_fish[key] = fish[key]


def move_fish():
    temp_fish = dict()
    for key in fish:
        # 여러방향의 물고기들
        for dkey in fish[key]:
            flag = 0
            for i in range(8):
                target = dkey - i
                if target < 0:
                    target += 8
                tempd = target % 8
                nx, ny = key[0] + dx[tempd], key[1] + dy[tempd]
                if 1 <= nx <= 4 and 1 <= ny <= 4 and (nx, ny) not in smell and (nx, ny) != (sx, sy):
                    flag = 1
                    if (nx, ny) in temp_fish:
                        if tempd in temp_fish[(nx, ny)]:
                            temp_fish[(nx, ny)][tempd] += fish[key][dkey]
                        else:
                            temp_fish[(nx, ny)][tempd] = fish[key][dkey]
                    else:
                        temp_fish[(nx, ny)] = {tempd: fish[key][dkey]}
                    break
            if flag == 0:
                if key in temp_fish:
                    if dkey in temp_fish[key]:
                        temp_fish[key][dkey] += fish[key][dkey]
                    else:
                        temp_fish[key][dkey] = fish[key][dkey]
                else:
                    temp_fish[key] = {dkey: fish[key][dkey]}

    fish.clear()
    for tkey in temp_fish:
        fish[tkey] = temp_fish[tkey]

def move_shark():
    global sx, sy
    max_fish = -1
    route = ''

    def dfs(cx, cy, fcnt, r, visited):
        global fish
        nonlocal max_fish, route

        if len(r) == 3:
            if max_fish < fcnt:
                max_fish = fcnt
                route = r
            return

        for i in range(4):
            nx, ny = cx + sdx[i], cy + sdy[i]
            if 1 <= nx <= 4 and 1 <= ny <= 4:
                if (nx, ny) in fish:
                    if (nx, ny) in visited:
                        dfs(nx, ny, fcnt, r + str(i + 1), visited)
                    else:
                        efish = 0
                        for dk in fish[(nx, ny)]:
                            efish += fish[(nx, ny)][dk]
                        visited.add((nx, ny))
                        dfs(nx, ny, fcnt + efish, r + str(i + 1), visited)
                        visited.remove((nx, ny))
                else:
                    dfs(nx, ny, fcnt, r + str(i + 1), visited)

    dfs(sx, sy, 0, '', set())

    for r in route:
        sx, sy = sx + sdx[int(r) - 1], sy + sdy[int(r) - 1]
        if (sx, sy) in fish:
            del fish[(sx, sy)]
            smell[(sx, sy)] = 2


def copied_fish_appear():

    for key in copied_fish:
        for cd in copied_fish[key]:
            if key in fish:
                if cd in fish[key]:
                    fish[key][cd] += copied_fish[key][cd]
                else:
                    fish[key][cd] = copied_fish[key][cd]
            else:
                fish[key] = {cd: copied_fish[key][cd]}

    copied_fish.clear()


def smell_check():
    temp_smell = dict()

    for key in smell:
        if 0 < smell[key]:
            temp_smell[key] = smell[key] - 1

    smell.clear()
    for sk in temp_smell:
        smell[sk] = temp_smell[sk]

def solution():

    for _ in range(s):
        # 1. 복제 마법
        copy_fish()
        # 2. 물고기 한칸 이동 (상어, 냄새, 격자 범위 넘으면 이동 X => 방향 전환 후 이동)
        move_fish()
        # 3. 상어는 상하좌우 연속 3칸 이동 가능 물고기 존재하면 다 사라지고 냄새만 남음
        move_shark()
        # 4. 냄새 2턴 이후 사라짐
        smell_check()
        # 5. 물고기 복제
        copied_fish_appear()

    answer = 0
    for key in fish:
        for dkey in fish[key]:
            answer += fish[key][dkey]
    print(answer)


    return 0

solution()