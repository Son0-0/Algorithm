from collections import deque


def solution(queue1, queue2):
    limit = len(queue1) * 2 + 1
    sum1, sum2 = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)

    cnt = 0
    while cnt <= limit:
        if sum1 == sum2:
            return cnt
        else:
            if sum1 < sum2:
                if queue2:
                    sum1 += queue2[0]
                    sum2 -= queue2[0]
                    queue1.append(queue2.popleft())
                else:
                    break
            else:
                if queue1:
                    sum2 += queue1[0]
                    sum1 -= queue1[0]
                    queue2.append(queue1.popleft())
                else:
                    break
        cnt += 1

    if sum1 == sum2:
        return cnt
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1, ], [1, 5]))
