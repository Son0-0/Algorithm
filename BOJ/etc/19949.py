import sys
input = sys.stdin.readline

ans = [num for num in list(map(int, input().split()))]

result = 0
def recur(count, odr_list, sum):
  if 5 < (count - sum):
    return
  
  if count == 10:
    if 5 <= sum:
      global result
      result += 1
    
    return
  
  for i in range(1, 6):
    if count > 1 and i == odr_list[count-1] == odr_list[count-2]:
      continue
    odr_list.append(i)
    if i == ans[count]:
      recur(count+1, odr_list, sum + 1)
    else:
      recur(count+1, odr_list, sum)
    odr_list.pop()
  
def solution():
  recur(0, [], 0)
  print(result)
  
solution()