import sys

input = sys.stdin.readline

n = int(input())
_map, slist = [], []
for r in range(n):
    temp = list(map(str, input().split()))
    for c, val in enumerate(temp):
        if val == 'S':
            slist.append([r, c])
    _map.append(temp)

vdict = dict()


def is_valid(target):

    # print(f'=========== {target} ===========')
    # for m in _map:
    #     print(*m)
    # print(f'=========== {target} ===========')

    flag = 1
    for s in slist:
        # 가로-왼쪽
        for i in range(s[1]):
            if _map[s[0]][i] == 'T':
                flag = 0
            elif _map[s[0]][i] == 'O':
                flag = 1

        if flag == 0:
            return False

        # 가로-오른쪽
        for i in range(n - 1, s[1], -1):
            if _map[s[0]][i] == 'T':
                flag = 0
            elif _map[s[0]][i] == 'O':
                flag = 1

        if flag == 0:
            return False

        # 세로-위쪽
        for i in range(s[0]):
            if _map[i][s[1]] == 'T':
                flag = 0
            elif _map[i][s[1]] == 'O':
                flag = 1

        if flag == 0:
            return False

        # 세로-아래쪽
        for i in range(n - 1, s[0], -1):
            if _map[i][s[1]] == 'T':
                flag = 0
            elif _map[i][s[1]] == 'O':
                flag = 1

        if flag == 0:
            return False

    return True


def dfs(x, y, cnt, visited):
    if cnt == 3:
        target = ''.join(sorted(visited))

        if target in vdict:
            return
        vdict[target] = 1

        if is_valid(target):
            print("YES")
            exit(0)
        return

    for i in range(n):
        for j in range(n):
            if _map[i][j] == 'X':
                _map[i][j] = 'O'
                dfs(i, j, cnt + 1, visited + [str(i) + str(j)])
                _map[i][j] = 'X'


def solution():

    dfs(0, 0, 0, [])

    print("NO")

    return 0


solution()
