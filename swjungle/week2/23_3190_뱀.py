import sys
from collections import deque

input = sys.stdin.readline

size = int(input())
_map = [[0] * size for _ in range(size)]
_map[0][0] = "*"

for _ in range(int(input())):
  x, y = map(int, input().split())
  _map[x - 1][y - 1] = 1

cmd = []
csize = int(input())
for _ in range(csize):
  cmd.append(list(input().split()))
cmd.append([10001, "D"]) # 마지막 명령어 다음 끝나는 것이 아니여야 하기 때문에 더미 값 추가

cur_d = 0

def dir_calc(dir):
  global cur_d
  
  if dir == "D":
    cur_d += 1
    if 0 <= cur_d:
      cur_d = cur_d % 4
    else:
      cur_d = 4 - (abs(cur_d) % 4)
  else:
    cur_d -= 1
    if 0 <= cur_d:
      cur_d = cur_d % 4
    else:
      cur_d = 4 - (abs(cur_d) % 4)
      
def solution():
  global cur_d
  cur_x, cur_y, cur_length = 0, 0, 1
  pos_queue = deque()
  pos_queue.append([0,0])
  
  sec = 0
  
  for idx in range(csize + 1):
    tsec, dir = int(cmd[idx][0]), cmd[idx][1]

    while sec < tsec and cur_x < size and cur_y < size:
      sec += 1
      
      if cur_d == 0:
        cur_y += 1
      elif cur_d == 1:
        cur_x += 1
      elif cur_d == 2:
        cur_y -= 1
      else:
        cur_x -= 1
      
      if cur_x < 0 or cur_y < 0 or size <= cur_x or size <= cur_y:
        print(sec)
        exit(0)
      
      pos_queue.append([cur_x, cur_y])
      if _map[cur_x][cur_y] == 1:
        pass
      elif _map[cur_x][cur_y] == "*":
        print(sec)
        exit(0)
      else:
        dq = pos_queue.popleft()
        _map[dq[0]][dq[1]] = 0
      
      _map[cur_x][cur_y] = "*"

      if _map[cur_x][cur_y] == 1:
        cur_length += 1
      
    dir_calc(dir)

  print(sec+1)
  
solution()