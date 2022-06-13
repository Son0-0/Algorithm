import sys

input = sys.stdin.readline

def solution():
  for _ in range(int(input())):
    coin_size = int(input())
    purse = list(map(int, input().split()))
    target = int(input())
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    
    for coin in purse:
      for idx in range(1, target + 1):
        if coin <= idx:
          dp[idx] += dp[idx - coin]
          
    print(dp[-1])
          
solution()