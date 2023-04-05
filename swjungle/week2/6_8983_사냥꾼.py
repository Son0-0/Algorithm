import sys

input = sys.stdin.readline

m, n, l = map(int, input().split())
hlist = [num for num in list(map(int, input().split()))]
hlist.sort()

alist = []
for _ in range(n):
  alist.append(list(map(int, input().split())))
alist.sort()

def calc(target, mid):
  if (abs(hlist[mid] - target[0]) + target[1]) <= l:
    return True
  return False

def bin_search(left, right, target):
  if right < left:
    return False
  
  mid = (left + right) // 2
  
  if calc(target, mid):
    return True
    
  if target[0] <= hlist[mid]:
    return bin_search(left, mid - 1, target)
  else:
    return bin_search(mid + 1, right, target)
    
def solution():
  global min_value
  cnt = 0
  for idx in range(n):
    if bin_search(0, m - 1, alist[idx]):
      cnt += 1
      
  print(cnt)

solution()

# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

# m, n, l = map(int, input().split())
# hlist = [num for num in list(map(int, input().split()))]
# alist = []
# for _ in range(n):
#   alist.append(list(map(int, input().split())))

# hlist.sort()
# alist.sort()

# def calc(hpos, target):
#   if abs(hlist[hpos]-target[0]) + target[1] <= l:
#     return True
#   return False

# def bin_search(left, right, target):
#   if right < left:
#     return False
  
#   mid = (left + right) // 2
  
#   if calc(mid, target):
#     return True

#   if target[0] <= hlist[mid]:
#     return bin_search(left, mid - 1, target)
#   else:
#     return bin_search(mid + 1, right, target)
  
# def solution():
#   cnt = 0
#   for idx in range(n):
#     if bin_search(0, m - 1, alist[idx]):
#       cnt += 1
  
#   print(cnt)
  
# solution()