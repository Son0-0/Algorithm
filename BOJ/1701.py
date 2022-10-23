import sys

input = sys.stdin.readline

text = input().rstrip()


def compute_lps(target):
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

    return max(lps)


def solution():
    answer = 0
    for i in range(len(text)):
        answer = max(answer, compute_lps(text[i:]))

    print(answer)


solution()
