import sys

input = sys.stdin.readline

size, b = map(int, input().split())
num_list = [[num for num in list(map(int, input().split()))] for _ in range(size)]

def calc(list_a, list_b):
  llist = [[0] * size for _ in range(size)]
  
  for row in range(size):
    for col in range(size):
      sum = 0
      for idx in range(size):
        sum += list_a[row][idx] * list_b[idx][col]
      llist[row][col] = sum % 1000
  
  return llist

def dq(_list, cnt):
  if cnt == 1:
    for row in range(size):
      for col in range(size):
        _list[row][col] %= 1000
    return _list
  
  target = dq(_list, cnt // 2)
  
  if cnt % 2 == 0:
    return calc(target, target)
  else:
    return calc(calc(target, target), _list)
        
def solution():
  for num in dq(num_list, b):
    print(*num)

solution()