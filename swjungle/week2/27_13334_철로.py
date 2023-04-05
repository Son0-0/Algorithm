import sys, heapq

input = sys.stdin.readline

hlist = []
for _ in range(int(input())):
  ho = list(map(int, input().split()))
  ho.sort()
  hlist.append(ho)
hlist.sort(key = lambda x : x[1])

d = int(input())

heap = []
max_value = 0

for h in hlist:
  if d < abs(h[0] - h[1]):
    continue
  
  if not heap:
    heapq.heappush(heap, h)
    continue
  
  while d < h[1] - heap[0][0]:
    heapq.heappop(heap)
    if not heap:
      break
  heapq.heappush(heap, h)
  max_value = max(max_value, len(heap))
  
print(max_value)