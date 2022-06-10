import sys, heapq

input = sys.stdin.readline

max_heap = []
min_heap = []

for _ in range(int(input())):
  num = int(input())
  if len(max_heap) == len(min_heap):
    heapq.heappush(max_heap, -num)
  else:
    heapq.heappush(min_heap, num)
    
  if max_heap and min_heap:
    if min_heap[0] < -max_heap[0]:
      max_num = heapq.heappop(max_heap)
      min_num = heapq.heappop(min_heap)
      heapq.heappush(max_heap, -min_num)
      heapq.heappush(min_heap, -max_num)
  
  print(-max_heap[0])