import sys

input = sys.stdin.readline

def solution():
  while True:
    size, target = map(int, input().split())
    if size == 0 and target == 0:
      return
    
    num_list = list(map(int, input().split()))
    prev = num_list[1]
    
    size = len(num_list)
    
    depth = [[] for _ in range(size + 1)]
    depth[1].append(num_list[0])
    
    cur_depth = 1
    target_depth = 0
    
    for num in num_list[1:]:
      if num == target:
        target_depth = cur_depth
        
      if prev + 1 == num:
        depth[cur_depth].append(num)
      else:
        cur_depth += 1
        depth[cur_depth].append(num)

      prev = num
    
    cnt, rng = 0, 1
    strt, end = 0, 0
    parent = 2
    llist = []
    for idx, d in enumerate(depth):
      if idx == parent:
        if parent < target_depth:
          strt = parent
        llist.append(parent)
        parent += len(d)
  
    if strt != 0:
      end = llist[llist.index(strt) + 1]
    answer = 0
    for idx in range(strt + 1, end + 1):
      if target in depth[idx]: continue
      answer += len(depth[idx])
      
    print(answer)
    
solution()