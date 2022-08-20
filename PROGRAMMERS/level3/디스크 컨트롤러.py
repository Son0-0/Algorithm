from heapq import heapify, heappush, heappop


def solution(jobs):
    size = len(jobs)
    
    heapify(jobs)

    cur = 0
    order = []
    while jobs:
        start, duration = heappop(jobs)
        if start < cur:
            temp = []
            heappush(temp, [duration, start])
            while jobs:
                if jobs[0][0] < cur:
                    a, b = heappop(jobs)
                    heappush(temp, [b, a])
                else:
                    break
            due, strt = heappop(temp)
            cur += due
            order.append(cur - strt)

            while temp:
                a, b = heappop(temp)
                heappush(jobs, [b, a])
        else:
            cur = start + duration
            order.append(duration)

    return int(sum(order) / size)


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 1], [1, 1], [50, 7]]))