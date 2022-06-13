import sys

input = sys.stdin.readline

N = int(input())

def solution():
  dp = [[0, 0], [0, 1], [1, 0]]
  
  for i in range(3, N + 1):
    dp.append([sum(dp[i - 1]), dp[i - 1][0]])
    
  print(sum(dp[N]))
  
solution()