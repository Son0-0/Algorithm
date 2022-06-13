import sys

input = sys.stdin.readline

A = list(map(str, input().strip()))
size_a = len(A)

B = list(map(str, input().strip()))
size_b = len(B)

bf = [0 for _ in range(size_a + 1)]
af = [0 for _ in range(size_a + 1)]


def solution():
    global af, bf
    result = [0, 0, 0]

    for row in range(1, size_b + 1):
        for col in range(1, size_a + 1):
            if A[col - 1] == B[row - 1]:
                af[col] = bf[col - 1] + 1
                if result[0] < af[col]:
                    result = [af[col], row, col]
            else:
                af[col] = 0
        bf = af

    print(result[0])

    for idx in range(result[2] - result[0], result[2]):
        print(A[idx], end='')


solution()