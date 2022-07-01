import sys

input = sys.stdin.readline

num_list = [
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
]

min_value = sys.maxsize

def is_prime(num):

  for i in range(2, int(num ** 0.5) + 1):
    if (num % i) == 0:
      return False
    
  return True

def dfs(num, target, idx, cnt):
  global min_value
  
  if 4 <= idx:
    return
    
  if num == target:
    min_value = min(min_value, cnt);
    return
    
  for i, tf in enumerate(num_list[idx]):
    temp_num = list(str(num))
    if tf == 0 and temp_num[idx] != str(i):
      print(i, tf)
      num_list[idx][i] = 1
      temp_num[idx] = str(i)
      temp_num = ''.join(temp_num)
      print(temp_num, idx)
      dfs(int(temp_num), target, idx + 1, cnt + 1)
      num_list[idx][i] = 0

def solution():
  global min_value
  
  for _ in range(int(input())):
    a, b = map(int, input().split())
    dfs(a, b, 0, 0)
    print(min_value)
    min_value = sys.maxsize
  
solution()