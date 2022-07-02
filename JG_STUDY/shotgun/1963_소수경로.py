import sys

input = sys.stdin.readline

min_value = sys.maxsize

def is_prime(num):

  for i in range(2, int(num ** 0.5)):
    if (num % i) == 0:
      return False
    
  return True

def dfs(num, target, idx, cnt):
  global min_value
  
  if 4 <= idx:
    return
    
  if num == target:
    print("here")
    min_value = min(min_value, cnt);
    return
  
  if is_prime(num):
    cnt += 1
  else:
    cnt -= 1
    
  for i in range(10):
    temp_num = list(str(num))
    
    if idx == 0 and i == 0:
      continue
    
    if temp_num[idx] != str(i):
      temp_num[idx] = str(i)
      temp_num = int(''.join(temp_num))
      dfs(temp_num, target, (idx + 1), cnt)

def solution():
  global min_value
  
  for _ in range(int(input())):
    a, b = map(int, input().split())
    dfs(a, b, 0, 0)
    print(min_value)
    min_value = sys.maxsize
  
solution()