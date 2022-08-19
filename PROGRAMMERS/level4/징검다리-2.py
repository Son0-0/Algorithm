import sys


def solution(distance, rocks, n):
    answer = 0

    rocks.sort()

    def calculate(mid):
        cur, cnt = 0, 0
        min_distance = sys.maxsize

        for rock in rocks:
            distance = rock - cur
            if distance < mid:
                cnt += 1
            else:
                cur = rock
                min_distance = min(min_distance, distance)

        return cnt, min_distance

    def binary_search(left, right):
        nonlocal answer

        if right < left:
            return

        mid = (left + right) // 2
        remove, distance = calculate(mid)

        if n < remove:
            binary_search(left, mid - 1)
        else:
            answer = distance
            binary_search(mid + 1, right)

    binary_search(0, distance)

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
