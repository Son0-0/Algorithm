import sys

input = sys.stdin.readline

def solution():
  while True:
    llist = [num for num in list(map(int, input().split()))]
    size = llist[0]
    if size == 0:
      break
    llist = llist[1:]
    
    stk = []
    ans = 0
    for idx in range(size):
      cur_height = llist[idx]
      
      if not stk:
        stk.append([cur_height, idx])
        continue
      else: # stk [height, idx]
        while stk and cur_height < stk[-1][0]:
          last_height = stk.pop()[0]
          if stk:
            ans = max(ans, (idx - stk[-1][1] - 1) * last_height)
          else:
            ans = max(ans, idx * last_height)
        stk.append([cur_height, idx])
        
    while stk:
      last = stk.pop()
      last_height, idx = last[0], last[1]
      if stk:
        ans = max(ans, (size - stk[-1][1] - 1) * last_height)
      else:
        ans = max(ans, size * last_height)
        
    print(ans)
solution()