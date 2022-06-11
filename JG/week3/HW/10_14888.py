import sys

max_value = -sys.maxsize - 1
min_value = sys.maxsize

size = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
llist = list(map(int, sys.stdin.readline().split()))

def calc(odr_list):
  global num, max_value, min_value
  result = num[0]
  
  odr_list = odr_list[::-1]
  
  for idx in range(len(num) - 1):
    if odr_list[idx] == 0:
      result += num[idx+1]
    elif odr_list[idx] == 1:
      result -= num[idx+1]
    elif odr_list[idx] == 2:
      result *= num[idx+1]
    else:
      if result < 0:
        result = (abs(result) // num[idx+1]) * -1
      else:
        result = result // num[idx+1]
      
  max_value = max(max_value, result)
  min_value = min(min_value, result)
    
def recur(visited, odr_list):
  global num
  if sum(visited) == sum(llist):
    calc(odr_list)
    return
  for idx in range(4):
    if llist[idx] != 0 and visited[idx] < llist[idx]:
      visited[idx] += 1
      odr_list.append(idx)
      recur(visited, odr_list)
      visited[idx] -= 1
      odr_list.pop()
    
def solution():
  global max_value, min_value
  visited = [0] * 4
  odr_list = []
  recur(visited, odr_list)
  
  print(max_value)
  print(min_value)
  
solution()