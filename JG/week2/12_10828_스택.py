import sys

input = sys.stdin.readline

stk = []
for _ in range(int(input())):
  cmd = list(input().split())
  
  if cmd[0] == "push":
    stk.append(int(cmd[1]))
  elif cmd[0] == "pop":
    if len(stk) != 0:
      print(stk.pop())
      continue
    print(-1)
  elif cmd[0] == "size":
    print(len(stk))
  elif cmd[0] == "empty":
    if len(stk) != 0:
      print(0)
      continue
    print(1)
  elif cmd[0] == "top":
    if len(stk) != 0:
      print(stk[-1])
      continue
    print(-1)