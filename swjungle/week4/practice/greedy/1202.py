import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jlist = [list(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]
jlist.sort()
bag.sort()


def solution():
    result = 0
    max_heap = []

    for b in bag:
        while jlist and jlist[0][0] <= b:
            heapq.heappush(max_heap, -jlist[0][1])
            heapq.heappop(jlist)

        if max_heap:
            result += -heapq.heappop(max_heap)
        elif not jlist:
            break

    print(result)


solution()