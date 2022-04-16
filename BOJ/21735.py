import sys

input = sys.stdin.readline
lsize, time = map(int, input().split())
llist = [num for num in list(map(int, input().split()))]
llist.insert(0, 0)
result = -sys.maxsize - 1

def recur(cur, size, count):
  if cur >= lsize or count == 0:
    global result
    result = max(result, size)
    return
  
  for idx in range(cur+1, cur+3):
    if cur < idx and idx <= lsize:
      if (idx-cur) == 1:
        recur(idx, size + llist[cur+1], count - 1)
      elif (idx - cur) == 2:
        recur(idx, int(size/2 + llist[cur+2]), count - 1)

def solution():
  recur(0, 1, time)
  print(result)
  
solution()