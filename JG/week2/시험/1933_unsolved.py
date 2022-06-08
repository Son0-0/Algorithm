import sys

input = sys.stdin.readline

size = int(input())
tower = []
for _ in range(size):
  l, h, r = map(int, input().split())
  tower.append([l, r, h])

def solution():
  stack = []
  for idx in range(size):
    if stack:
      if stack[-1][2] < tower[idx][2]:
        pos_tower = stack.pop()
        stack.append([pos_tower[0], tower[idx][1], pos_tower[2]])
        stack.append(tower[idx])
      else:
        stack.append([stack[-1][1], tower[idx][1], tower[idx][2]])
    stack.append(tower[idx])
  print(stack)
        
solution()