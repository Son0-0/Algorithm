# import sys

# n, m = list(map(int, sys.stdin.readline().split()))

# llist = []
# llist = list(map(int, sys.stdin.readline().split()))

# result = []

# def recur(visited, lsum, count):
#   if count == 3:
#     if lsum <= m:
#       result.append(lsum)
#     return
#   else:
#     for i in range(n):
#       if visited[i] == 0:
#         visited[i] = 1
#         count += 1
#         lsum += llist[i]
#         recur(visited, lsum, count)
#         count -= 1
#         visited[i] = 0
#         lsum -= llist[i]
    
# def solution():
#   global result
  
#   visited = [0] * n
#   count = 0
#   lsum = 0
  
#   recur(visited, lsum, count)
#   result = list(set(result))
#   print(max(result))
    
  
# solution()

import sys

size, num = map(int, sys.stdin.readline().split())
llist = list(map(int, sys.stdin.readline().split()))
min_value = sys.maxsize
result = 0

def recur(visited, count, sum):
  global min_value
  global result

  if count == 0:
    if min_value > (num - sum) and sum <= num:
      min_value = (num - sum)
      result = sum
    return

  for idx in range(size):
    if visited[idx] == 0:
      visited[idx] = 1
      recur(visited, count - 1, sum + llist[idx])
      visited[idx] = 0

def solution():
  visited = [0] * size
  recur(visited, 3, 0)
  print(result)

solution()