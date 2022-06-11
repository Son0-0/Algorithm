import sys, heapq

input = sys.stdin.readline

n, k = map(int, input().split())
queue = []
coin = []
for _ in range(n):
  coin.append(int(input()))
coin = list(set(coin))
coin.sort(reverse=True)
visited = [0 for _ in range(k + 1)]

def bfs():
  while queue:
    cnt, pos = heapq.heappop(queue)
    for c in coin:
      npos = pos + c
      if npos == k:
        return cnt + 1
      if npos < k and visited[npos] == 0:
        visited[npos] = 1
        heapq.heappush(queue, (cnt + 1, npos))

def solution():
  heapq.heappush(queue, (0, 0)) # coin, position
  count = bfs()
  if count:
    print(count)
  else:
    print(-1)
    
solution()