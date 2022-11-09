import sys, heapq

input = sys.stdin.readline

n, k = map(int, input().split())


def solution():
    
    if k <= n:
        print(n - k)
        return

    q = []
    heapq.heappush(q, [0, n])
    
    visited = dict()
    visited[n] = 1
    
    while q:
        ct, cp = heapq.heappop(q)
        
        if cp == k:
            print(ct)
            return
            
        for pos in [cp * 2, cp + 1, cp - 1]:
            if 0 <= pos < 100001 and pos not in visited:
                visited[pos] = 1
                if pos == cp * 2:
                    heapq.heappush(q, [ct, pos])
                    q.append([ct, pos])
                else:
                    heapq.heappush(q, [ct + 1, pos])
                    q.append([ct + 1, pos])
    
solution()