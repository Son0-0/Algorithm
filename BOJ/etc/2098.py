import sys

input = sys.stdin.readline
size = int(input())
llist = []
for _ in range(size):
  llist.append(list(map(int, input().split())))
min_value = sys.maxsize

def recur(start, cur, visited, cost):
  global min_value
  
  if min_value < cost:
    return
  
  if sum(visited) == size:
    target = llist[cur][start]
    if target != 0:
      min_value = min(min_value, cost+target)
      return
  
  for i in range(size):
    target = llist[cur][i]
    if visited[i] == 0 and target != 0:
        visited[i] = 1
        recur(start, i, visited, cost+target)
        visited[i] = 0
  
def solution():
  visited = [0] * size
  for i in range(size):
    visited[i] = 1
    recur(i, i, visited, 0)
    visited[i] = 0
  
  print(min_value)
  
solution()