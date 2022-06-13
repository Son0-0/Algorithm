import sys

input = sys.stdin.readline


def solution():
    for _ in range(int(input())):
        num_size = int(input())
        plist = list(reversed(list(map(int, input().split()))))
        result, max_value = 0, plist[0]

        for idx in range(num_size):
            if plist[idx] <= max_value:
                result += max_value - plist[idx]
            else:
                max_value = plist[idx]

        print(result)


solution()