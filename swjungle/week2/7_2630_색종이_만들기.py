import sys

input = sys.stdin.readline

size = int(input())
paper = [list(map(int, input().split())) for _ in range(size)]
blue_cnt, white_cnt = 0, 0

def is_blue_or_white(pp, N): # 합이 (N**2)//2 일때 + 1 return
  global blue_cnt, white_cnt  

  target = 0

  for p in pp:
    target += sum(p)

  if target == (N**2):
    blue_cnt += 1
    return
  elif target == 0:
    white_cnt += 1
    return
  else:
    half = int(N/2)
    pp1 = [p[0:half] for p in pp[0:half]]
    is_blue_or_white(pp1, half)
    
    pp2 = [p[half:N] for p in pp[0:half]]
    is_blue_or_white(pp2, half)
    
    pp3 = [p[0:half] for p in pp[half:N]]
    is_blue_or_white(pp3, half)
    
    pp4 = [p[half:N] for p in pp[half:N]]
    is_blue_or_white(pp4, half)
  
def solution():
  is_blue_or_white(paper, size)
  print(white_cnt)
  print(blue_cnt)
  
solution() 

# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

# size = int(input())

# _map = []
# for _ in range(size):
#   _map.append(list(map(int,input().split())))

# blue_cnt = 0
# white_cnt = 0

# def recur(smap, size):
#   global white_cnt, blue_cnt
#   psum = 0
  
#   for paper in smap:
#     psum += sum(paper)

#   if psum == size**2:
#     blue_cnt += 1
#     return
#   elif psum == 0:
#     white_cnt += 1
#     return
#   else:
#     half = size // 2
    
#     p1 = [pp[0:half] for pp in smap[0:half]]
#     recur(p1, half)
    
#     p2 = [pp[half:size] for pp in smap[0:half]]
#     recur(p2, half)
    
#     p3 = [pp[0:half] for pp in smap[half:size]]
#     recur(p3, half)
    
#     p4 = [pp[half:size] for pp in smap[half:size]]
#     recur(p4, half)
    

# def solution():
#   recur(_map, size)
#   print(white_cnt)
#   print(blue_cnt)
  
# solution()