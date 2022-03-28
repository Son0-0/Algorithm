import sys, heapq

input = sys.stdin.readline

size = int(input())
max_heap = []
for _ in range(size):
  for num in list(map(int, input().split())):
    heapq.heappush(max_heap, -num)
    
print(-max_heap[size - 1])