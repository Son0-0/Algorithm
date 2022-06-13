import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
elist = list(map(int, input().split()))
q = []


def isExist(e):  # 현재 큐에 해당 전기용품이 있는지 체크 있다면 return True
    same = 0

    for idx in range(len(q)):
        temp = q[idx][1]

        if temp == e:
            same += 1

        if temp in elist:
            q[idx][0] = -elist.index(temp)
        else:
            q[idx][0] = -K

        heapq.heappush(q, heapq.heappop(q))

    if same == 0:
        return False
    return True


def solution():
    cnt = 0
    for idx in range(K):
        temp, elist[idx] = elist[idx], 0  # temp에 현재 사용할 전기용품 저장, elist에는 0으로

        if isExist(temp):  # 멀티탭에 이미 있으면 pass
            continue

        if N <= len(q):  # 멀티탭 full 이면 pop 후 cnt + 1
            cnt += 1
            heapq.heappop(q)

        if temp in elist[idx + 1:]:  # 이후 1회 이상 사용할경우
            heapq.heappush(
                q, [-elist.index(temp), temp])  # 이후 해당 전기용품 사용하는 index 기준으로 정렬되게 q에 push
        # 이후 사용할 경우가 없다면 index를 -K로 큐 맨 앞에 넣기 (이후 사용할 일이 없으니 pop할 때 제일 처음으로 되도록)
        else:
            heapq.heappush(q, [-K, temp])

    print(cnt)


solution()