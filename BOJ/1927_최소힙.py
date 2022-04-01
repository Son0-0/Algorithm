import sys, heapq

input = sys.stdin.readline

min_heap = []
for _ in range(int(input())):
  data = int(input())
  
  if data == 0:
    if len(min_heap) != 0:
      print(min_heap[0])
      heapq.heappop(min_heap)
    else:
      print(0)
  else:
    heapq.heappush(min_heap, data)