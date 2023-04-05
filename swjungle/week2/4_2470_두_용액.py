import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

size = int(input())
num_list = [num for num in list(map(int, input().split()))]
num_list.sort()

min_value = sys.maxsize
result = [0, 0]
def bin_search(left, right):
  global min_value, result
  
  if right <= left:
    return

  target = num_list[left] + num_list[right]
  
  if abs(target) < min_value:
    min_value = abs(target)
    result[0], result[1] = num_list[left], num_list[right]
    
  if target == 0:
    print(num_list[left], num_list[right])
    return
  elif target < 0:
    return bin_search(left+1, right)
  else:
    return bin_search(left, right-1)
    
def solution():
  bin_search(0, size-1)
  print(*result, sep=" ")
  
solution()

# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

# size = int(input())
# llist = [num for num in list(map(int, input().split()))]
# llist.sort()

# min_value = sys.maxsize
# result = [0, 0]
# def bin_search(left, right):
#   global min_value, result
  
#   if right <= left:
#     return
  
#   mid = llist[left] + llist[right]
  
#   if abs(mid) < min_value:
#     result[0], result[1] = llist[left], llist[right]
#     min_value = abs(mid)
  
#   if mid == 0:
#     print(llist[left], llist[right])
#     return

#   if mid < 0:
#     bin_search(left+1, right)
#   else:
#     bin_search(left, right-1)
  
# def solution():
#   bin_search(0, size - 1)
#   print(*result)

# solution()