import sys

input = sys.stdin.readline
n, k = map(int, input().split())
level_list = [int(input()) for _ in range(n)]
level_list.sort()

max_val = -sys.maxsize - 1
def calc(target):
  sum = 0
  for level in level_list:
    if level < target:
      sum += target - level
      
  return sum

def bin_search(left, right):
  if right < left:
    return
  
  mid = (left + right) // 2
  
  if calc(mid) <= k:
    global max_val
    max_val = max(max_val, mid)
    bin_search(mid + 1, right)
  else:
    bin_search(left, mid - 1)
  
def solution():
  bin_search(level_list[0], level_list[-1] + k)
  print(max_val)
  
solution()

# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

# n, k = map(int, input().split())
# llist = []
# for _ in range(n):
#   llist.append(int(input()))
# llist.sort()
# result = 0

# def calc(level):
#   sum = k
#   for c in llist:
#     sum -= level - c
#     if sum < 0:
#       return False
  
#   return True

# def bin_search(left, right):
#   if right < left:
#     return
  
#   mid = (left + right) // 2
  
#   if calc(mid):
#     global result
#     result = max(result, mid)
#     return bin_search(mid + 1, right)
#   else:
#     return bin_search(left, mid - 1)
  
# def solution():
#   bin_search(llist[0], llist[-1] + k)
#   print(result)
  
# solution()