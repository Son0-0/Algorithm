# ref: https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence
import sys

input = sys.stdin.readline

list_a = list(map(str, input().strip()))
size_a = len(list_a)

list_b = list(map(str, input().strip()))
size_b = len(list_b)

llist = [[0 for _ in range(size_a + 1)] for _ in range(size_b + 1)]


def solution():
    for row in range(1, size_b + 1):
        for col in range(1, size_a + 1):
            if list_a[col - 1] == list_b[row - 1]:
                llist[row][col] = llist[row - 1][col - 1] + 1
            else:
                llist[row][col] = max(llist[row - 1][col], llist[row][col - 1])

    print(llist[-1][-1])


solution()