import sys

def solution(a, b, g, s, w, t):
    answer = sys.maxsize

    def calc(target):
        cg, cs, ca = 0, 0, 0
        for idx, time in enumerate(t):
            cnt = target // (time * 2)
            if time <= (target % (time * 2)):
                cnt += 1

            cg += g[idx] if g[idx] < cnt * w[idx] else cnt * w[idx]
            cs += s[idx] if s[idx] < cnt * w[idx] else cnt * w[idx]
            ca += g[idx] + s[idx] if (g[idx] + s[idx]) < cnt * w[idx] else cnt * w[idx]

        if a <= cg and b <= cs and a + b <= ca:
            nonlocal answer
            answer = min(answer, target)
            return True
        return False

    def binary_search(left, right):
        if right < left:
            return

        mid = (left + right) // 2
        result = calc(mid)

        if result == True:
            binary_search(left, mid - 1)
        else:
            binary_search(mid + 1, right)

        return 0

    max_time = max(t)
    binary_search(0, (a + b) * max_time * 2)

    return answer


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
