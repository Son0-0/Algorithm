import heapq

def solution(jobs):
    hq = []
    rlist = []
    estimate_end_time = 0
    
    for j in jobs:
        heapq.heappush(hq, j)
    
    temp = []
    while hq:
        if hq[0][0] <= estimate_end_time:
            cur = heapq.heappop(hq)
            heapq.heappush(temp, [cur[1], cur[0]])
        else:
            if not temp:
                cur = heapq.heappop(hq)
                heapq.heappush(temp, [cur[1], cur[0]])
                continue
            while temp:
                cur = heapq.heappop(temp)
                if cur[1] <= estimate_end_time:
                    estimate_end_time += cur[0]
                    rlist.append(estimate_end_time - cur[1])
                else:
                    estimate_end_time = cur[1] + cur[0]
                    rlist.append(estimate_end_time - cur[1])
    while temp:
        cur = heapq.heappop(temp)
        if cur[1] <= estimate_end_time:
            estimate_end_time += cur[0]
            rlist.append(estimate_end_time - cur[1])
        else:
            estimate_end_time = cur[1] + cur[0]
            rlist.append(estimate_end_time - cur[1])
    
    return (sum(rlist) // len(jobs))
