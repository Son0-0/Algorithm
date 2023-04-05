# https://www.acmicpc.net/problem/2447
import sys

input = sys.stdin.readline


def star(length):

    if length == 3:
        return ['***', '* *', '***']

    part = star(length // 3)
    answer = []

    for p in part:
        answer.append(p * 3)

    for p in part:
        answer.append(p + ' ' * (length // 3) + p)

    for p in part:
        answer.append(p * 3)

    return answer


def solution():

    answer = star(int(input()))
    print('\n'.join(answer))

    return 0


solution()
