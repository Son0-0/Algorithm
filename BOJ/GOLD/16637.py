import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
l = []
s = list(map(str, input().strip()))
answer = -sys.maxsize

if len(s) == 1:
    print(s[0])
    exit(0)

for idx, val in enumerate(s):
    if not val.lstrip('-').isdigit():
        l.append(idx)


def is_valid(oplist: list):
    for i in range(len(oplist) - 1):
        if oplist[i + 1] - oplist[i] == 2:
            return False

    return True


def calc_part(op, num1, num2):
    return {
        '+': lambda: num1 + num2,
        '-': lambda: num1 - num2,
        '*': lambda: num1 * num2,
    }.get(op, lambda: None)()


def calc(target: list):
    num = -1

    for idx, val in enumerate(target):
        if not val.lstrip('-').isdigit():
            num = calc_part(val, num, int(target[idx+1]))
        else:
            if idx == 0:
                num = int(val)

    global answer
    answer = max(answer, num)


def solution():
    for length in range(len(l)):
        for oplist in combinations(l, length):
            if is_valid(oplist):
                temp = [st for st in s]
                for i, pos in enumerate(oplist):
                    idx = pos - (i * 2)
                    n = calc_part(temp[idx],
                                  int(temp[idx-1]), int(temp[idx + 1]))
                    temp = temp[:idx - 1] + [str(n)] + temp[idx+2:]
                calc(temp)

    print(answer)


solution()
