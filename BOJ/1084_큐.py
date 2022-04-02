
import sys
from collections import deque
input = sys.stdin.readline

n = deque()
for _ in range(int(input())):
  cmd = list(input().split())
  command = cmd[0]
  
  if command == "push":
    n.append(cmd[1])
  elif command == "pop":
    if n:
      print(n.popleft())
    else:
      print(-1)
  elif command == "size":
    print(len(n))
  elif command == "empty":
    if n:
      print(0)
    else:
      print(1)
  elif command == "front":
    if n:
      print(n[0])
    else:
      print(-1)
  else:
    if n:
      print(n[-1])
    else:
      print(-1)