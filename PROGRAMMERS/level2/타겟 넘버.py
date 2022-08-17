from itertools import permutations


def solution(numbers, target):
    answer = 0

    size = len(numbers)

    def dfs(cur, value):
        nonlocal answer

        if cur == size:
            if value == target:
                answer += 1
            return

        dfs(cur + 1, value + numbers[cur])
        dfs(cur + 1, value - numbers[cur])

    dfs(0, 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
