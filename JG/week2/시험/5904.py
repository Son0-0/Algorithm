import sys

input = sys.stdin.readline

def dc(cnt, moo, N):
  left = (moo - cnt - 3) // 2
  right = left + cnt + 3
  
  if N <= left: # (moo) mooo moo
    return dc(cnt - 1, left, N) 
  elif right < N: # moo mooo (moo)
    return dc(cnt - 1, left, N - right)
  else: # moo (mooo) moo
    if N - left == 1:
      return "m"
    else:
      return "o"
    
def solution():
  N = int(input())  
  moo = 3
  cnt = 0
  
  while moo < N:
    cnt += 1 
    moo = (moo * 2) + (cnt + 3)

  print(dc(cnt, moo, N))
  
solution()