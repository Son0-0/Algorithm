import sys, heapq

input = sys.stdin.readline

size = int(input())

_map = [[num for num in list(map(int, input().split()))] for _ in range(size)]

cnt = [0, 0, 0]
def dq(llist, size):
  if size == 1:
    cnt[llist[0][0]] += 1
    return
  
  s_cnt = 0
  strt = llist[0][0]

  for row in range(size):
    for col in range(size):
      if strt == llist[row][col]:
        s_cnt += 1
      else:
        s_cnt = -1
        break  
  
  if s_cnt == size*size:
    cnt[strt] += 1
  else:
    div = size // 3 # 9 -> 3
    
    pp1 = [p[0:div] for p in llist[0:div]]
    pp2 = [p[div:size - div] for p in llist[0:div]]
    pp3 = [p[size - div:size] for p in llist[0:div]]
    
    pp4 = [p[0:div] for p in llist[div:size-div]]
    pp5 = [p[div:size - div] for p in llist[div:size-div]]
    pp6 = [p[size - div:size] for p in llist[div:size-div]]
    
    pp7 = [p[0:div] for p in llist[size-div:size]]
    pp8 = [p[div:size - div] for p in llist[size-div:size]]
    pp9 = [p[size - div:size] for p in llist[size-div:size]]

    dq(pp1, div)
    dq(pp2, div)
    dq(pp3, div)
    
    dq(pp4, div)
    dq(pp5, div)
    dq(pp6, div)
    
    dq(pp7, div)
    dq(pp8, div)
    dq(pp9, div)
    
dq(_map, size)
print(cnt[-1])
print(cnt[0])
print(cnt[1])