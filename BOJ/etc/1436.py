import sys

def solution():
    num = int(sys.stdin.readline())
    count = 0
    dnum = 666
    while num != count:
        if "666" in str(dnum):
            count += 1
        dnum += 1
    print(dnum - 1)

solution()