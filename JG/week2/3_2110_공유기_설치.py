
import sys

input = sys.stdin.readline

n, c = map(int, input().split())
house_list = [int(input()) for _ in range(n)]
house_list.sort()
max_value = -sys.maxsize - 1

def calc(target):
  start, cnt = 0, 1
  for idx in range(1,n):
    if target <= (house_list[idx] - house_list[start]):
      cnt += 1
      start = idx

  if c <= cnt:
    return True
  return False
  
def bin_search(left, right):
  if right < left:
    return
  
  mid = (left + right) // 2
  
  if calc(mid) == True:
    global max_value
    max_value = max(max_value, mid)
    return bin_search(mid+1, right)
  else:
    return bin_search(left, mid-1)
    
def solution():
  bin_search(1, house_list[-1] - house_list[0])
  print(max_value)
  
solution()