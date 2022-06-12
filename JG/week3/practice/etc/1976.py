import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
odr_list = list(map(int, input().split()))
parents = [num for num in range(N + 1)]

def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])
  return parents[x]

def union(x, y):
  a, b = find(x), find(y)
  
  if a < b:
    parents[b] = a
  else:
    parents[a] = b
  
def solution():
  for i in range(N):
    for j in range(N):
      if city[i][j] == 1:
        union(i+1, j+1)
  
  conn = find(odr_list[0])
  for idx in range(1, M):
    if parents[odr_list[idx]] != conn:
      print("NO")
      return
  print("YES")
  
solution()