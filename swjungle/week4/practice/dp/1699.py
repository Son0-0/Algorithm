import sys

input = sys.stdin.readline

def solution():
  N = int(input())
  dp = [0, 1]
  for i in range(2, N + 1):
    if (i ** 0.5) ** 2 == i:
      dp.append(1)
    else:
      dp.append(dp[i - 1] + 1)
  
  print(dp)
  print(dp[N])
  
solution()