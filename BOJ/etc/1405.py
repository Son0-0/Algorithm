import sys

input = sys.stdin.readline
plist = [num for num in list(map(int, input().split()))]
count = plist[0]
plist = plist[1:]
map = [[0]*29 for i in range(29)]

result = 0

def recur(cur_x, cur_y, cnt, perc):
  if perc == 0:
    return
  
  if cnt == 0:
    global result
    result += perc
    return
  
  for i in range(4): # 동 서 남 북 E W S N
    if i == 0:
      if map[cur_x][cur_y+1] == 0:
        map[cur_x][cur_y] = 1
        recur(cur_x, cur_y+1, cnt - 1, perc * plist[i]/100)
        map[cur_x][cur_y] = 0
    elif i == 1:
      if map[cur_x][cur_y-1] == 0:
        map[cur_x][cur_y] = 1
        recur(cur_x, cur_y-1, cnt - 1, perc * plist[i]/100)
        map[cur_x][cur_y] = 0
    elif i == 2:
      if map[cur_x-1][cur_y] == 0:
        map[cur_x][cur_y] = 1
        recur(cur_x-1, cur_y, cnt - 1, perc * plist[i]/100)
        map[cur_x][cur_y] = 0
    else:
      if map[cur_x+1][cur_y] == 0:
        map[cur_x][cur_y] = 1
        recur(cur_x+1, cur_y, cnt - 1, perc * plist[i]/100)
        map[cur_x][cur_y] = 0
  
def solution():
  recur(14, 14, count, 1)
  print(result)
  
solution()