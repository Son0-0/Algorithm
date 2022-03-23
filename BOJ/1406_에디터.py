import sys
input = sys.stdin.readline

stc = list(input().rstrip())

stk = []
for _ in range(int(input())):
  cmd = list(input().split())

  if cmd[0] == 'L':
    if 0 < len(stc):
      stk.append(stc.pop())
  elif cmd[0] == 'D':
    if 0 < len(stk):
      stc.append(stk.pop())
  elif cmd[0] == 'B':
    if 0 < len(stc):
      stc.pop()
  elif cmd[0] == 'P':
    stc.append(cmd[1])
  
for _ in range(len(stk)):
  stc.append(stk.pop())

print(*stc, sep="")