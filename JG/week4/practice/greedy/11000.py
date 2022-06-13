import sys
import heapq

input = sys.stdin.readline

N = int(input())
llist = []
for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(llist, (a, b))


def solution():
    q = []
    heapq.heappush(q, heapq.heappop(llist)[1])

    while llist:
        lec = heapq.heappop(llist)
        if lec[0] < q[0]:
            heapq.heappush(q, lec[1])
        else:
            heapq.heappop(q)
            heapq.heappush(q, lec[1])

    print(len(q))


solution()