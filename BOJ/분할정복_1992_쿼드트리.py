import sys

input = sys.stdin.readline

size = int(input())
_map = [list(map(int, input().rstrip())) for _ in range(size)]

def dq(llist, size):  
  result = ""
  if size == 1:
    return str(sum(llist[0]))
  
  psum = 0
  for row in llist: 
    psum += sum(row)
    
  if psum == 0:
    return "0"
  elif psum == size**2:
    return "1"
  else:
    half = size // 2
    
    pp1 = [p[0:half] for p in llist[0:half]]
    pp2 = [p[half:size] for p in llist[0:half]]
    pp3 = [p[0:half] for p in llist[half:size]]
    pp4 = [p[half:size] for p in llist[half:size]]
    
    result += "(" + dq(pp1, half)
    result += dq(pp2, half)
    result += dq(pp3, half)
    result += dq(pp4, half) + ")"
    
  return result

print(dq(_map, size))