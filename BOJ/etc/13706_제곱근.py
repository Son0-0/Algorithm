import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
target = int(input())

def bin_search(left, right):
  if right < left:
    return
  
  mid = (left + right) // 2
  
  cnum = mid**2
  if cnum == target:
    print(mid)
    return mid
  elif cnum < target:
    return bin_search(mid+1, right)
  else:
    return bin_search(left, mid-1)
  
bin_search(1, target//2)