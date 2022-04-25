import sys
import heapq

input = sys.stdin.readline

sangmin_time, jisoo_time, N = map(int, input().split())
pnum = 0


def solution():
    pq = []
    sptr, jptr = 0, 0
    scnt, jcnt = 0, 0
    for _ in range(N):
        t, color, count = map(str, input().split())
        t, count = int(t), int(count)
        if color == 'B':
            sptr = max(sptr, t)
            for _ in range(count):
                scnt += 1
                heapq.heappush(pq, (sptr, 'B'))
                sptr += sangmin_time
        else:
            jptr = max(jptr, t)
            for _ in range(count):
                jcnt += 1
                heapq.heappush(pq, (jptr, 'R'))
                jptr += jisoo_time

    cnt = 1
    sangmin_list, jisoo_list = [], []
    while pq:
        dummy, color = heapq.heappop(pq)
        if color == 'B':
            sangmin_list.append(cnt)
        else:
            jisoo_list.append(cnt)
        cnt += 1

    print(scnt)
    print(*sangmin_list, sep=' ')

    print(jcnt)
    print(*jisoo_list, sep=' ')

    return 0


solution()
