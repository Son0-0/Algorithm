import sys

input = sys.stdin.readline
size = int(input())
clist = [num for num in list(map(int, input().split()))]
budget = int(input())
max_value = -sys.maxsize - 1

def calc(target):
  global max_value
  sum = 0 
  for c in clist:
    if c < target:
      sum += c
    else:
      sum += target
  if sum <= budget:
    max_value = max(max_value, target)
  return sum
  
def bin_search(left, right):
  mid = (left + right) // 2
  
  if right < left:
    return
  
  if calc(mid) <= budget:
    return bin_search(mid+1, right)
  else:
    return bin_search(left, mid-1)
  
def solution():
  bin_search(0, max(clist))
  print(max_value)
  
solution()