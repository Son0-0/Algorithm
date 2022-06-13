import sys

input = sys.stdin.readline

def solution():
  numlist = input().strip().split('-')

  num = []
  for 5n in numlist:
    temp = n.split('+')
    temp_sum = 0
    for tnum in temp:
      temp_sum += int(tnum)
    num.append(temp_sum)
    
  result = num[0]
  for snum in num[1:]:
    result -= snum
    
  print(result)
  
solution()