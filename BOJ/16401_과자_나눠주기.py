import sys

input = sys.stdin.readline

M, N = map(int, input().split())
llist = [num for num in list(map(int, input().split()))]
llist.sort()
max_value = -1

def calc(target):
  if target == 0:
    return False
  
  cnt = 0
  for l in llist:
    if target <= l:
      cnt += (l // target)

    if M <= cnt:
      return True

  return False

def bin_search(left, right):
  if right < left:
    return
  
  mid = (left + right) // 2
  
  if calc(mid):
    global max_value
    max_value = max(max_value, mid)
    bin_search(mid + 1, right)
  else:
    return bin_search(left, mid - 1)
  
def solution():
  bin_search(0, max(llist))
  if max_value == -1:
    print(0)
    return
  print(max_value)

solution()