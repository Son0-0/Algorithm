import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

size = int(input())
paper = [[c for c in list(map(str, input().strip()))] for _ in range(size)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_rgb(x, y, cur_color):
  paper[x][y] = "*"

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < size and 0 <= ny < size:
      if paper[nx][ny] == cur_color:
        dfs_rgb(nx, ny, cur_color)
    
def dfs_b(x, y, temp_map, cur_color):
  temp_map[x][y] = "*"
  
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < size and 0 <= ny < size:
      if temp_map[nx][ny] != "*":
        if cur_color == "B":
          if temp_map[nx][ny] == "B":
            dfs_b(nx, ny, temp_map, cur_color)
        elif cur_color == "R" or cur_color == "G":
          if temp_map[nx][ny] != "B":
            dfs_b(nx, ny, temp_map, cur_color)
  
  return temp_map
  
def solution():
  temp = [[c for c in clr] for clr in paper]
  cnt = 0
  for row in range(size):
    for col in range(size):
      if temp[row][col] != "*":
        temp = dfs_b(row, col, temp, temp[row][col])
        cnt += 1
  
  rgb_cnt = 0
  for row in range(size):
    for col in range(size):
      if paper[row][col] != "*":
        dfs_rgb(row, col, paper[row][col])
        rgb_cnt += 1
        
  print(rgb_cnt)
  print(cnt)

solution()