import sys

input = sys.stdin.readline

size, target_length = map(int, input().split())
tlist = [*(map(int, input().split()))]

def calc(mid):
  sum = 0
  for tree in tlist:
    if mid < tree:
      sum += (tree-mid)
  
  return sum
    
def solution():
  left, right = 0, max(tlist)
  
  while left <= right:
    mid = (left + right) // 2
    
    if target_length <= calc(mid):
      left = mid + 1
    else:
      right = mid - 1
      
  print(right)
        
solution()

# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# tree = [num for num in list(map(int, input().split()))]
# tree.sort()
# max_value = 0

# def calc(target):
#   sum = 0
#   for t in tree:
#     if target < t:
#       sum += t - target

#     if m <= sum:
#       return True
#   return False

# def bin_search(left, right):
#   if right < left:
#     return
  
#   mid = (left + right) // 2
  
#   if calc(mid):
#     global max_value
#     max_value = max(max_value, mid)
#     return bin_search(mid + 1, right)
#   else:
#     return bin_search(left, mid - 1)
  
# def solution():
#   bin_search(0, tree[-1])
#   print(max_value)
  
# solution()