# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7

import  sys
input = sys.stdin.readline

size = int(input())
_map = [list(map(int, input().split())) for _ in range(size)]

min_v = max(map(max, _map)) # 2차원 배열 최소 값
max_v = min(map(min, _map)) # 2차원 배열 최대 값
    
# result = 0
# def recur(x, y, d):
#   for i in range(y+1, size-1):
#     if _map[x][y] > d:
#       recur(x, y+1, d)
#       recur(x+1, y, d)
#     global result
#     result += 1
  
# def solution():
#   visited = [[0] * size for _ in range(size)]
#   recur(0, 0, 5)
#   print(result)
  
  
# solution()