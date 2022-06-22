import sys

input = sys.stdin.readline


def solution():

    a_length, b_length = map(int, input().split(' '))

    a_list = list(map(int, input().split(' ')))
    b_list = list(map(int, input().split(' ')))

    print(*sorted(a_list + b_list))


solution()