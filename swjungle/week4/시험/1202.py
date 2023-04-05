import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jwl = [list(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]

jwl.sort()
bag.sort()


def solution():

    tq = []
    result = 0

    for idx in range(K):
        while jwl:  # 가방에 담을 수 있는 최대 무게랑 같거나 가벼운 보석 탐색
            jw = heapq.heappop(jwl)
            if jw[0] <= bag[idx]:
                heapq.heappush(tq, -jw[1])  # 가벼운 보석의 가치만 tq에 push
            else:
                heapq.heappush(jwl, jw)  # 무겁다면 다시 jwl에 넣어줌
                break

        if tq:  # tq에 보석이 있다면 제일 가치가 높은 보석을 result에 더해줌
            result += -heapq.heappop(tq)

    print(result)


solution()