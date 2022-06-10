import sys, heapq

input = sys.stdin.readline

num_heap = []
size = int(input())
if size == 1:
  print(0)
else:
  for _ in range(size):
    num = int(input())
    heapq.heappush(num_heap, num)

  result = 0
  while 1 < len(num_heap):
    sum = heapq.heappop(num_heap) + heapq.heappop(num_heap)
    result += sum
    heapq.heappush(num_heap, sum)
  
  print(result)
  
  import sys, heapq

# input = sys.stdin.readline

# size = int(input())

# num = []
# for _ in range(size):
#   heapq.heappush(num, int(input()))
  
# if size < 2:
#   print(0)
# elif 2 <= len(num):
#   result = 0
#   while num:
#     a, b = heapq.heappop(num), heapq.heappop(num)
#     if not num:
#       result += a + b
#       break
#     else:
#       result += a + b
#       heapq.heappush(num, a + b)
#   print(result)