import sys
import heapq

input = sys.stdin.readline


def solution():
    min_heap = []

    for _ in range(int(input())):
        nums = list(map(int, input().split()))
        if not min_heap:
            for num in nums:
                heapq.heappush(min_heap, num)

        else:
            for num in nums:
                if min_heap[0] < num:
                    heapq.heappush(min_heap, num)
                    heapq.heappop(min_heap)

    print(min_heap[0])


solution()