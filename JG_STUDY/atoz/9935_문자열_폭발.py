import sys

input = sys.stdin.readline


def solution():

    target = list(input().strip())[::-1]
    bomb = list(input().strip())
    bomb_len = len(bomb)

    stack = []

    while target:
        stack.append(target.pop())
        if stack[-(bomb_len):] == bomb:
            for _ in range(bomb_len):
                stack.pop()

    print(*stack, sep='') if stack else print("FRULA")


solution()