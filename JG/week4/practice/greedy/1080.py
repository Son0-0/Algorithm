import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A, B = [], []

for _ in range(N):
    A.append(list(map(int, input().strip())))
for _ in range(N):
    B.append(list(map(int, input().strip())))


def reverse(x, y):
    if N < x + 3 or M < y + 3:
        return False

    for row in range(x, x + 3):
        for col in range(y, y + 3):
            A[row][col] = 0 if A[row][col] == 1 else 1

    return True


def solution():
    cnt = 0

    if A == B:
        print(cnt)
        return

    for row in range(N):
        for col in range(M):
            if A[row][col] != B[row][col]:
                if reverse(row, col):
                    cnt += 1
                    if A == B:
                        print(cnt)
                        return

    print(-1)


solution()