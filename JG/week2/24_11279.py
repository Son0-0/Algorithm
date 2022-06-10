import sys, heapq

input = sys.stdin.readline

max_heap = []
for _ in range(int(input())):
  cmd = int(input())
  if cmd == 0:
    if len(max_heap) == 0:
      print(0)
    else:
      print(-heapq.heappop(max_heap))
  else:
    heapq.heappush(max_heap, -cmd)

# import sys

# input = sys.stdin.readline

# max_heap = []

# def insert_max_heap(num):
#   global max_heap
#   max_heap.append(num)
  
#   parent = len(max_heap) - 1

#   while parent != 0:
#     if max_heap[parent // 2] < max_heap[parent]:
#       max_heap[parent // 2], max_heap[parent] = max_heap[parent], max_heap[parent // 2]
#       parent = parent // 2
#     else:
#       break
    
# def delete_max_heap():
#   global max_heap
  
#   max_heap[-1], max_heap[0] = max_heap[0], max_heap[-1]
#   max_heap.pop()
  
#   if len(max_heap) < 3:
#     return
  
#   cur = 0  
#   while cur < len(max_heap):
#     if (cur*2 + 1) < len(max_heap):
#       if max_heap[cur] > max_heap[cur*2+1]: # and max_heap[cur] > max_heap[cur*2+2]:
#         break
#       else: 
#         max_heap[cur*2+1], max_heap[cur] = max_heap[cur], max_heap[cur*2+1]
#         cur = cur*2 + 1
#         continue
#     elif (cur*2 + 2) < len(max_heap):
#       if max_heap[cur] > max_heap[cur*2+2]:
#         break
#       elif max_heap[cur*2+2] > max_heap[cur]:
#         max_heap[cur*2+2], max_heap[cur] = max_heap[cur], max_heap[cur*2+2]
#         cur = cur*2 + 2

# def solution():
#   for _ in range(int(input())):
#     cmd = int(input())
    
#     if cmd == 0:
#       if len(max_heap) == 0:
#         print(0)
#       else:
#         print(max_heap[0])
#         delete_max_heap()
#     else:
#       insert_max_heap(cmd)

# solution()