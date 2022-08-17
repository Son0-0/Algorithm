from heapq import heappop, heappush, heapify


def solution(scoville, K):
    answer = 0

    heapify(scoville)

    while scoville and scoville[0] < K:
        t1 = heappop(scoville)
        
        if scoville:
            t2 = heappop(scoville)
            target = t1 + t2 * 2
            answer += 1
            heappush(scoville, target)
        else:
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))