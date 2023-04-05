import sys
from collections import deque

input = sys.stdin.readline


def solution():

    target = list(map(str, input().strip()))
    n = int(input())

    stack = []
    for i in range(n):
        cmd = list(map(str, input().split()))

        if cmd[0] == 'L':
            if target:
                stack.append(target.pop())
        elif cmd[0] == 'D':
            if stack:
                target.append(stack.pop())
        elif cmd[0] == 'B':
            if target:
                target.pop()
        else:
            target.append(cmd[1])

    print(*(target + stack[::-1]), sep='')


solution()
