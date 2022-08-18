from collections import deque


def solution(queue1, queue2):
    answer = 0

    size = len(queue1)

    q1, q2 = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)

    if q1 == q2:
        return answer

    while answer <= size * 2 + 1 and q1 != q2:
        if q1 < q2:
            temp = queue2.popleft()
            queue1.append(temp)
            q1 += temp
            q2 -= temp
        else:
            temp = queue1.popleft()
            queue2.append(temp)
            q2 += temp
            q1 -= temp
        answer += 1

    if q1 != q2:
        return -1
    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
