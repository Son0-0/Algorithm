# def isPnum(num):
#   count = 0
  
#   for i in range(1, num + 1):
#     if (num % i) == 0:
#       count += 1
#     if count > 2:
#       return False
  
#   if count == 2:
#     return True
  
# case_size = int(input())

# for i in range(0, case_size):
#   num = int(input())
#   strg = [num//2] * 2

#   for k in range(0, num//2):
#     if isPnum(strg[0]) == True and isPnum(strg[1]) == True:
#       print(strg[0], strg[1])
#       break
    
#     strg[0] -= 1
#     strg[1] += 1

import sys

pnum = [num for num in range(10001)]

def eratos():
  global pnum
  pnum[1] = 0

  for idx in range(10001):
    if pnum[idx] != 0:
      for i in range(idx*2, 10001, idx):
        pnum[i] = 0

def solution():
  eratos()
  for _ in range(int(sys.stdin.readline())):
    _input = int(sys.stdin.readline())

    for idx in range(_input // 2, 0, -1):
      if pnum[idx] != 0 and pnum[_input - idx] != 0:
        print(idx, _input-idx)
        break

solution()