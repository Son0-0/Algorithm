import sys

input = sys.stdin.readline


def is_pseudo(l, r, target):
    while l < r:
        if target[l] != target[r]:
            return False
        l += 1
        r -= 1

    return True


def solution():

    for _ in range(int(input())):
        target = input().rstrip()

        length = len(target)
        answer = 0

        # 회문인지 판단 후 아니면 answer를 유사회문으로 초기화
        for i in range(length // 2):
            if target[i] != target[length - 1 - i]:
                answer = 1

        if answer == 0:
            print(0)
            continue

        l, r = 0, length - 1
        while l < r:
            if target[l] != target[r]:
                if not is_pseudo(l + 1, r, target) and not is_pseudo(l, r - 1, target):
                    answer = 2
                break
            else:
                l += 1
                r -= 1
        print(answer)


solution()
