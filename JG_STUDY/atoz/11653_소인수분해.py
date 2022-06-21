import sys

input = sys.stdin.readline

def solution():
  
  num = int(input())
  div_num = 2
  
  while 1 < num:
    if (num % div_num) == 0:
      num //= div_num
      print(div_num)
    else:
      div_num += 1
  
solution()