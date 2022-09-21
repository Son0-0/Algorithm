import sys

input = sys.stdin.readline

n = int(input())
l = sorted(list(map(int, input().split())))


def solution():

    for i in range(n + 1):
        temp = [num for num in l]

        flag = 1
        for _ in range(i):
            if temp.pop() < i:
                flag = 0
                break

        if flag == 0:
            continue

        for _ in range(n - i):
            if i < temp.pop():
                flag = 0
                break

        if flag == 1:
            print(i)
            return


solution()
