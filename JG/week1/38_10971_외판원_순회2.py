import sys

_map = []
result = sys.maxsize
size = int(sys.stdin.readline())

def recur(visited: list, odr_list: int, cost: int):
  global result
  if result < cost:
    return

  if sum(visited) == len(visited):
    target = _map[odr_list[-1]][odr_list[0]]
    if target != 0:
      result = min(result, cost+target)
      return

  for idx in range(size):
    target = _map[odr_list[-1]][idx]
    if visited[idx] == 0 and target != 0:
      visited[idx] = 1
      odr_list.append(idx)
      recur(visited, odr_list, cost + target)
      odr_list.pop()
      visited[idx] = 0

def solution():
  global _map

  for _ in range(size):
    _map.append(list(map(int, sys.stdin.readline().split())))

  for idx in range(size):
    visited = [0] * size
    odr_list = [idx]
    visited[idx] = 1
    recur(visited, odr_list, 0)
    odr_list.clear()

  print(result)

solution()

# import sys

# size = int(sys.stdin.readline())

# a = [[0]*size]*size

# for idx in range(size):
#   a[idx] = list(map(int, sys.stdin.readline().split()))

# result = sys.maxsize

# def recur(start, cur, visited, cost):
#   if start == cur and sum(visited) == len(visited):
#     global result
#     result = min(result, cost)
#     return
#   for i in range(size):
#     if visited[i] == 0 and a[cur][i] != 0:
#       visited[i] = 1
#       recur(start, i, visited, cost+a[cur][i])
#       visited[i] = 0

# def solution():
#   global result
  
#   visited = [0] * size
#   cost = 0
#   recur(0, 0, visited, cost)
  
#   print(result)
  
# solution()

# import sys
# input = sys.stdin.readline
# size = int(input())
# llist = [list(map(int, input().split())) for _ in range(size)]
# min_value = sys.maxsize

# def recur(visited, odr_list, cost):
#   global min_value
  
#   if min_value < cost:
#     return
  
#   if sum(visited) == size:
#     target = llist[odr_list[-1]][odr_list[0]]
#     if target != 0:
#       cost += target
#       min_value = min(min_value, cost)
#       return
  
#   for i in range(size):
#     if visited[i] == 0:
#       target = 0
#       if 0 < len(odr_list):
#         target = llist[odr_list[-1]][i]
#         if target == 0:
#           continue
#       visited[i] = 1
#       recur(visited, odr_list + [i], cost + target)
#       visited[i] = 0
      
# def solution():
#   visited = [0] * size
#   recur(visited, [], 0)
#   print(min_value)
  
# solution()