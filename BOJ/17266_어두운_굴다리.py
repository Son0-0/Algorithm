import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
llist = [num for num in list(map(int, input().split()))]
min_value = sys.maxsize

def calc(height):
  if M == 1:
    if 0 < llist[0] - height or llist[0] + height < N:
      return False
    else:
      return True
  
  for idx in range(M):
    if idx == 0:
      if 0 < llist[idx] - height or llist[idx] + height < llist[idx + 1] - height:
        return False
      continue
    
    if idx == M - 1:
      if llist[idx] + height < N or llist[idx - 1] + height < llist[idx] - height:
        return False
      continue
    
    if llist[idx-1] + height < llist[idx] - height or llist[idx] + height < llist[idx+1] - height:
      return False

  return True

def bin_search(left, right):
  if right < left:
    return 
  
  mid = (left + right) // 2

  if calc(mid):
    global min_value
    min_value = min(min_value, mid)
    return bin_search(left, mid - 1)
  else:
    return bin_search(mid + 1, right)
    
def solution():
  bin_search(1, max(N-min(llist), max(llist)))
  print(min_value)
  
solution()