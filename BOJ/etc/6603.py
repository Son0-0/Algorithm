import sys

input = sys.stdin.readline

llist = []
size = 0

result = []
def recur(cur, rs):
  if len(rs) == 6:
    print(*rs, sep=" ")
    result.append(rs[:])
    return
  
  for i in range(cur+1, len(llist)):
    recur(i, rs + [llist[i]])
  
def solution():
  while True:
    global llist, result, size
    llist = [num for num in list(map(int, input().split()))]
    size = llist[0]
    
    if size == 0:
      break
  
    llist = llist[1::]
    recur(-1, [])
    print()
    result.clear()
  
solution()