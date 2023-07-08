from heapq import heappop, heappush, heapify


def fillCups(amount) -> int:
    answer, q = 0, []

    for water in amount:
        heappush(q, -water)

    while q[0] != 0:
        a, b = -heappop(q), -heappop(q)
        heappush(q, -(a - 1)), heappush(q, -(b - 1))
        answer += 1

    return answer


print(fillCups([1, 4, 2]) == 4)
print(fillCups([5, 4, 4]) == 7)
