import sys

input = sys.stdin.readline

def solution():
  for _ in range(int(input())):
    dp = [1, 2, 4]
    
    n = int(input())
    
    if n == 1:
      print(1)
      continue
    elif n == 2:
      print(2)
      continue
    elif n == 3:
      print(4)
      continue
    else:
      for i in range(n - 3):
        dp.append(dp[i] + dp[i + 1] + dp [i + 2])
    
    print(dp[-1])
    
solution()