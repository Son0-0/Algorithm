# https://school.programmers.co.kr/learn/courses/30/lessons/67259

import sys
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]    

def solution(board):
  answer = sys.maxsize
  
  q = deque()
  q.append([0, 0, 0, 0])
  q.append([0, 0, 1, 0])
  N = len(board)
  
  while q:
    cx, cy, cs, cc = q.popleft() # cur_x, cur_y, cur_state, cur_cost
    if cx == N - 1 and cy == N - 1:
      answer = min(answer, cc)
      
    for i in range(4):
      nx, ny = cx + dx[i], cy + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        if -1 <= board[nx][ny] < 1:
          board[nx][ny] -= 1
          if cs == 0 and 0 <= i < 2:
            q.append([nx, ny, 0, cc + 100])
          elif cs == 0 and 2 <= i < 4:
            q.append([nx, ny, 1, cc + 600])
          elif cs == 1 and 0 <= i < 2:
            q.append([nx, ny, 0, cc + 600])
          else:
            q.append([nx, ny, 1, cc + 100])
    
  return answer
  
print('=>', solution([[0,0,0],[0,0,0],[0,0,0]]))
print('=>', solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print('=>', solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print('=>', solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))