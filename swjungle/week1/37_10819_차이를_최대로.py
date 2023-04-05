n = int(input())

llist = []
llist = list(map(int, input().split()))

result = []
def sumlist(odrlist):
  global result
  
  sum = 0
  for idx in range(len(odrlist) - 1):
    sum += abs(odrlist[idx] - odrlist[idx+1])
    
  result.append(sum)
    
def recur(visited, count, odr):
  if count == n:
    sumlist(odr)
    return
  
  for idx in range(n):
    if visited[idx] == 0:
      visited[idx] = 1
      odr.append(llist[idx])
      recur(visited, count+1, odr)
      odr.pop()
      visited[idx] = 0


def solution():
  global result
  
  visited = [0] * n
  count = 0
  odr = []
  
  recur(visited, count, odr)
  
  print(max(result))
  
solution()