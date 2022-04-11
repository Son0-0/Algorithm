import sys
input = sys.stdin.readline

result = []

def recur(visited, count, data, org):
  if count == 0:
    global result
    result.append(data)
    return
  
  for i in range(len(visited)):
    if visited[i] == 0:
      visited[i] = 1
      recur(visited, count - 1, data + org[i], org)
      visited[i] = 0

def solution():
  while True:
    try:
      target, pos = input().split()

      visited = [0] * len(target)
      recur(visited, len(target), "", target)

      if len(result) < int(pos):
        print(f"{target} {pos} = No permutation")
      else:
        print(f"{target} {pos} = {result[int(pos) - 1]}")
      
      result.clear()
    except:
      return
  
solution()