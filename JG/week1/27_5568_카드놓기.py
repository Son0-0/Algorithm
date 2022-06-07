import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

result = []
llist = []

for _ in range(n):
  llist.append(sys.stdin.readline().rstrip())

def recur(visited, cnum, count):
  global result 

  if count == 0:
    result.append(cnum)
    return

  for i in range(n):
    if visited[i] == 0:
      visited[i] = 1
      recur(visited, cnum + llist[i], count-1)
      visited[i] = 0

def solution():
  global result

  visited = [0] * n
  recur(visited, "", k)
  result = list(set(result))
  print(len(result))

solution()