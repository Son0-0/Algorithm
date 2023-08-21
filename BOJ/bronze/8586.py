import sys
import re

input = sys.stdin.readline


def solution():
    _ = input()
    target = input().strip()

    for i in range(26):
        target = target.replace(chr(ord("a") + i), " ")
        target = target.replace(chr(ord("A") + i), " ")

    _sum = 0
    for num in target.split(" "):
        if num:
            _sum += int(num)

    return _sum


print(solution())


# def solution():
#     _ = int(input())

#     _sum = 0
#     for num in re.sub(r"[a-zA-Z]", " ", input().strip()).split(" "):
#         if num:
#             _sum += int(num)

#     return _sum


# print(solution())
