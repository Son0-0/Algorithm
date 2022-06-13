import sys

input = sys.stdin.readline

def solution():
  dp = [0, 1, 2]
  n = int(input())
  
  for idx in range(3, n + 1):
    dp.append((dp[idx - 2] + dp[idx - 1]) % 10007)
  
  print(dp[n] % 10007)

solution()