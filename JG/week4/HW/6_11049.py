import sys

input = sys.stdin.readline

N = int(input())
llist = []

for _ in range(N):
  llist.append(list(map(int, input().split())))

def solution():
  dp = [[0 for _ in range(N)] for _ in range(N)]
  
  for i in range(N - 1):
    dp[i][i + 1] = llist[i][0] * llist[i][1] * llist[i + 1][0]
      
  for i in range(1, N):
    for j in range(N - i):
      dp[j][j + i] = sys.maxsize
      for k in range(j, j+i): 
        dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + llist[j][0] * llist[k][1] * llist[j+i][1])
  
  print(dp[0][N - 1])
  
solution()

# 4
# 2 3
# 3 2
# 2 6
# 6 1