from collections import deque


def solution(priorities, location):
    answer = 0

    comp = deque(sorted(priorities, reverse=True))
    priorities = deque([[num, idx] for idx, num in enumerate(priorities)])

    while priorities and comp:
        temp = priorities.popleft()
        if comp[0] <= temp[0]:
            comp.popleft()
            answer += 1
            if location == temp[1]:
                return answer
        else:
            priorities.append(temp)


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
