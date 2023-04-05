import sys

input = sys.stdin.readline

N = int(input())
rlist = list(map(int, input().split()))
flist = list(map(int, input().split()))  # 주유소 리터 당 가격


def solution():

    result = 0
    cur_f = 1000000001

    for idx in range(N - 1):
        cur_f = min(cur_f, flist[idx])
        result += rlist[idx] * cur_f

    print(result)


solution()