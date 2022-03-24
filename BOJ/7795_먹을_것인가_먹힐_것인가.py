import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
result = 0
list_b = []
list_a = []
    
def bin_search(left, right, target):
  if right < left:
    return
  
  mid = (left + right) // 2
  
  if list_b[mid] < target:
    global result
    result = mid
    return bin_search(mid + 1, right, target)
  else:
    return bin_search(left, mid - 1, target)
  
  recur(mid + 1, right)
  recur(left, mid - 1)
  
  
def solution():
  for _ in range(int(input())):
    n, m = map(int, input().split())
    global list_a, list_b
    list_a = [num for num in list(map(int, input().split()))]
    list_b = [num for num in list(map(int, input().split()))]
    
    list_a.sort()
    list_b.sort()
    
    sum = 0
    for target in list_a:
      global result
      result = -1
      bin_search(0, m - 1, target)
      if result != -1:
        sum += result + 1

    print(sum)
    
    list_a.clear()
    list_b.clear()
    
solution()