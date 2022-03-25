import sys
input = sys.stdin.readline

size = int(input())
num_list = [num for num in list(map(int, input().split()))]
num_list.sort()

csize = int(input())
cnum_list = [num for num in list(map(int, input().split()))]

result = []
def bin_search(left, right, target):
  global result
  
  if right < left:
    print("0", end=" ")
    return
  
  mid = (left + right) // 2
  
  mid_num = num_list[mid]
  if mid_num == target:
    print("1", end=" ")
    return
  elif mid_num < target:
    return bin_search(mid + 1, right, target)
  else:
    return bin_search(left, mid - 1, target)

def solution():
  for num in cnum_list:
    bin_search(0, size - 1, num)
  
solution()