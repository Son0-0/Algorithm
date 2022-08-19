import sys

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()

    def calc(target):
        prev, remove = 0, 0
        min_distance = sys.maxsize

        for rock in rocks:
            distance = rock - prev
            if target <= distance:
                min_distance = min(min_distance, distance)
                prev = rock
            else:
                remove += 1
                if n < remove:
                    return False, min_distance
        return True, min_distance

    def binary_search(left, right):
        if right < left:
            return

        mid = (left + right) // 2

        result, value = calc(mid)

        if result == True:
            nonlocal answer
            answer = max(answer, value)
            binary_search(mid + 1, right)
        else:
            binary_search(left, mid - 1)

    binary_search(0, distance)

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
