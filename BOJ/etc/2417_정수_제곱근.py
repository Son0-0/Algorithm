import sys

input = sys.stdin.readline
min_value = sys.maxsize
target = int(input())

def bin_search(left, right):
  global min_value
  
  if right < left:
    return
  
  mid = (left + right) // 2
  
  if target == mid*mid:
    min_value = mid
    return
  elif target < mid*mid:
    min_value = min(min_value, mid)
    return bin_search(left, mid - 1)
  else:
    return bin_search(mid + 1, right)
    
def solution():
  bin_search(0, target)
  print(min_value)
  
solution()