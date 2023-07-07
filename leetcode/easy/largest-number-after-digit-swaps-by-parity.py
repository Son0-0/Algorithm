from heapq import heappush, heappop
from collections import deque


def largestInteger(num: int) -> int:
    odd, even = [], []
    index = deque()

    while num != 0:
        temp = num % 10

        if temp % 2 == 0:
            heappush(even, temp)
            index.appendleft(0)
        else:
            heappush(odd, temp)
            index.appendleft(1)

        num //= 10

    answer, cnt = 0, 0
    while index:
        cur = index.pop()

        if cur == 0:
            temp = heappop(even)
        else:
            temp = heappop(odd)

        answer += temp * (10**cnt)
        cnt += 1

    return answer


print(largestInteger(1234))
print(largestInteger(65875))
