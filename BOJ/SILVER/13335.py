import sys
from collections import deque

input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = deque(map(int, input().split()))


def solution():

    answer, cs = 0, 0
    on_road = deque([0 for _ in range(w)])

    while truck:
        cs -= on_road.popleft()
        if cs + truck[0] <= l:
            on_road.append(truck.popleft())
            cs += on_road[-1]
        else:
            on_road.append(0)
        answer += 1

    while cs != 0:
        cs -= on_road.popleft()
        answer += 1

    print(answer)


solution()
