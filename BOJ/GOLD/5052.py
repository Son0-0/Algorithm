import sys

input = sys.stdin.readline


def solution():

    for _ in range(int(input())):
        phone_number = []
        size = 0
        for _ in range(int(input())):
            phone_number.append(input().strip())
            size += 1
        phone_number.sort()

        flag = 1
        for idx in range(size - 1):
            length = len(phone_number[idx])
            if phone_number[idx] == phone_number[idx + 1][:length]:
                print("NO")
                break
        else:
            print("YES")

    return 0


solution()
