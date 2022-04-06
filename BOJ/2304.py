# import sys

# input = sys.stdin.readline

# N = int(input())
# hlist = [list(map(int, input().split())) for _ in range(N)]
# hlist.sort()

# def solution():

#   p, result = 0, 0
#   for idx in range(N):
#     if hlist[p][1] < hlist[idx][1]:
#       result += hlist[idx][1] * (hlist[idx][0] - hlist[p][0])
#       p = idx
#     else:
#       result += hlist[p][1]
#     print(idx, result)

#   if p != (N - 1):
#     print("reamin", p)


#   print(hlist)
#   print(result)


# solution()

import sys
input = sys.stdin.readline

N = int(input())
hlist = [list(map(int, input().split())) for _ in range(N)]
hlist.sort()


def solution():
    height = 0
    left = 0
    answer = 0

    for h in hlist:
        if height <= h[1]:
            answer += (h[0] - left)*height
            height = h[1]
            left = h[0]

    height = 0
    left = 0
    hlist.reverse()
    for h in hlist:
        if height <= h[1]:
            answer += (left - h[0])*height
            height = h[1]
            left = h[0]
    left = 0
    h_t = 0
    for h in hlist:
        if height == h[1]:
            answer -= (left - h[0])*h_t
            left = h[0]
            h_t = h[1]
    answer += height
    print(answer)


solution()
