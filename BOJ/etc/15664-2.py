import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [int(num) for num in input().split()]
result = []
num_list.sort()

def recur(cur, rs):
  if len(rs) == m:
    if rs in result:
      return
    result.append(rs)
    return
  
  for i in range(cur+1, n):
    recur(i, rs + [num_list[i]])

def solution():
  global result
  recur(-1, [])
  for m in result:
    print(*m, sep=" ")

solution()