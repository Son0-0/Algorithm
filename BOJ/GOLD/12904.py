import sys

input = sys.stdin.readline


def solution():

    s = input().strip()
    t = input().strip()

    while len(s) != len(t):
        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1][::-1]

    if s == t:
        print(1)
    else:
        print(0)


solution()
