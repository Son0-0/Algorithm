import sys

input = sys.stdin.readline


def solution():
    llist = [[] for _ in range(9)]
    max_len = 0

    for idx in range(int(input())):
        temp = list(map(str, input().strip()))[::-1]
        max_len = max(max_len, len(temp))

        for idx in range(1, len(temp) + 1):
            llist[idx].append(temp[idx - 1])

    strg = {}
    for idx in range(max_len, 0, -1):
        for i in llist[idx]:
            if not i in strg:
                strg[i] = 10**(idx - 1)
            else:
                strg[i] += 10**(idx - 1)

    result = 0
    strt = 9

    for num in sorted(strg.items(), key=lambda item: item[1], reverse=True):
        result += num[1] * strt
        strt -= 1

    print(result)


solution()
