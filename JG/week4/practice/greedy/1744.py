import sys

input = sys.stdin.readline

def solution():
  num_p = []
  num_n = []
  for _ in range(int(input())):
    temp = int(input())
    if temp <= 0:
      num_n.append(temp)
    else:
      num_p.append(temp)

  num_p.sort(reverse=True)
  num_n.sort()
  
  print(num_p)
  print(num_n)
    
solution()