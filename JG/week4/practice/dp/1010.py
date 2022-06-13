import sys

input = sys.stdin.readline

def solution():
  dp = [[0 for _ in range(31)] for _ in range(31)]
  
  for row in range(31):
    for col in range(31):
      if row == col:
        dp[row][col] = 1
        continue
      
      dp[row][col] = dp[row][col - 1] + dp[row - 1][col - 1]
  
  for _ in range(int(input())):
    a, b = map(int, input().split())
    print(dp[a][b])
    
solution()