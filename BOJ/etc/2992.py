import sys
input = sys.stdin.readline

num = input().rstrip()
size = len(num)
min_value = sys.maxsize

def recur(visited, count, nnum):
  if num[0] == "0":
    return
  
  if count == 0:
    if int(num) < int(nnum):
      global min_value
      min_value = min(min_value, int(nnum))
  
  for i in range(size):
    if visited[i] == 0:
      visited[i] = 1
      recur(visited, count - 1, nnum + str(num[i]))
      visited[i] = 0
    
  
def solution():
  visited = [0] * size
  recur(visited, size, "")
  if min_value == sys.maxsize:
    print(0)
    return
  print(min_value)

solution()