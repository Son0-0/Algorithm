import sys


def solution(n, times):
    answer = sys.maxsize
    times.sort(reverse=True)

    def calc(target):
        cnt = 0

        for time in times:
            cnt += (target // time)

        if cnt < n:
            return False
        return True

    def binary_search(left, right):
        if right < left:
            return

        mid = (left + right) // 2
        result = calc(mid)

        if result == True:
            nonlocal answer
            answer = min(answer, mid)
            binary_search(left, mid - 1)
        else:
            binary_search(mid + 1, right)

    binary_search(0, n * times[0])

    return answer


print(solution(6, [7, 10]))
