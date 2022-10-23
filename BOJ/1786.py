import sys

input = sys.stdin.readline

text = input().rstrip()
target = input().rstrip()


def compute_lps():
    lps = [0 for _ in range(len(target))]

    length, i = 0, 1
    while i < len(target):
        if target[i] == target[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp():
    answer = []

    lps = compute_lps()

    m, n = len(target), len(text)
    i, j = 0, 0
    while i < n:
        if target[j] == text[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == m:
            answer.append(i - j + 1)
            j = lps[j - 1]

    return answer


def solution():
    answer = kmp()

    print(len(answer))
    if len(answer) != 0:
        print(*answer)


solution()
