import sys 

input = sys.stdin.readline

n = int(input())

def solution():
  dp = [0, 1, 3]
  
  for i in range(3, n + 1):
    dp.append((dp[i - 1] + 2 * dp[i - 2]) % 10007)
  
  print(dp[n])
  
solution()