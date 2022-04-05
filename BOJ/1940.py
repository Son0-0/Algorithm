# https://www.acmicpc.net/problem/1940

N = int(input())
M = int(input())
llist = list(map(int, input().split()))
llist.sort()


def solution():
    p1, p2 = 0, N - 1

    cnt = 0
    while p1 < p2:
        nsum = llist[p1] + llist[p2]
        if nsum < M:
            p1 += 1
        elif M < nsum:
            p2 -= 1
        else:
            cnt += 1
            p1 += 1
            p2 -= 1

    print(cnt)


solution()
