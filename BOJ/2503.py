import sys
input = sys.stdin.readline
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

plist = []
def recur(visited, count, rs):
  if count == 0:
    plist.append(rs)
    return
  
  for i in range(9):
    if visited[i] == 0:
      visited[i] = 1
      recur(visited, count - 1, rs + str(num[i]))
      visited[i] = 0

def solution():
  visited = [0] * 9
  recur(visited, 3, "")
  
  for _ in range(int(input())):
    global plist
    num, s, b = map(int, input().split())
    num = str(num)

    for idx in range(len(plist)):
      s_cnt = 0
      b_cnt = 0
      for i in range(3):
        if plist[idx] == "":
          continue
        if num[i] == plist[idx][i]:
          s_cnt += 1
        elif plist[idx].count(num[i]) == 1:
          b_cnt += 1
          
      if s_cnt != s or b_cnt != b:
        plist[idx] = ""
  plist = list(set(plist))
  if "" in plist:  
    print(len(plist) - 1)
    return
  print(len(plist))
         
solution()