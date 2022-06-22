from audioop import reverse
import sys

input = sys.stdin.readline


def calc(mul, target):

    str_to_int = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }

    result = 0

    if mul == 8:
        for idx, num in enumerate(reversed(target[1:])):
            result += (str_to_int[num] * 8 ** idx)
    else:
        for idx, num in enumerate(reversed(target[2:])):
            result += (str_to_int[num] * 16 ** idx)

    return result


def solution():

    num = list(map(str, input().strip()))

    if num[1] == 'x':
        print(calc(16, num))
        return
    elif num[0] == '0':
        print(calc(8, num))
        return
    else:
        print(*num, sep='')


solution()
