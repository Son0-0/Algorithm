import sys

input = sys.stdin.readline

def solution():
  N = int(input())
  num = list(map(int, input().split()))

  dp = [n for n in num]
  
  for i in range(1, N):
    for j in range(i):
      if num[j] < num[i]:
        dp[i] = max(dp[i], num[i] + dp[j])
      
  print(max(dp))
      
solution()