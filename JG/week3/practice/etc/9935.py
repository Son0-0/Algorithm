import sys

input = sys.stdin.readline

target = list(input().strip())
bomb = list(input().strip())

def solution():
  stack = []
  
  for idx in range(len(target)):
    stack.append(target[idx])
    if len(bomb) <= len(stack):
      if stack[-len(bomb)::] == bomb:
        for _ in range(len(bomb)):
          stack.pop()

  if len(stack) == 0:
    print("FRULA")
    return
  print(*stack, sep='')
      
solution()