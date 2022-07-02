import sys
from itertools import permutations

input = sys.stdin.readline

n, k = map(int, input().split())
mlist = [[] for _ in range(n)]

for idx, val in enumerate(list(map(int, input().split()))):
  mlist[idx].append(val)
for idx, val in enumerate(list(map(int, input().split()))):
  mlist[idx].append(val)


def solution():

    answer = 0

    for case in list(permutations([num for num in range(n)], n)):
        temp_k, temp_p = k, 0

        for town in case:
            if mlist[town][0] < temp_k:
                temp_p += mlist[town][1]
                temp_k -= mlist[town][0]
                answer = max(answer, temp_p)
            else:
                break

    print(answer)


solution()