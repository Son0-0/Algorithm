# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

# num = []

# def postorder(s, e):
#   if e < s:
#     return
  
#   temp = e + 1
#   for idx in range(s + 1, e + 1):
#     if num[s] < num[idx]:
#       temp = idx
#       break
     
#   postorder(s + 1, temp - 1)
#   postorder(temp, e)
#   print(num[s])
  
# def solution():
#   while True:
#     try:
#       num.append(int(input()))
#     except:
#       break
    
#   postorder(0, len(num) - 1)
  
# solution()

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

num = []

def postorder(s, e):
  if e < s:
    return
  
  temp = e + 1
  for idx in range(s + 1, e + 1):
    if num[s] < num[idx]:
      temp = idx
      break
    
  postorder(s + 1, temp - 1)
  postorder(temp, e)
  print(num[s])

def solution():
  while True:
    try:
      num.append(int(input()))
    except:
      break
    
  postorder(0, len(num) - 1)
  
solution()