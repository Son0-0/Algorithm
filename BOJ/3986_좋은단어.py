import sys

input = sys.stdin.readline

stk = []

count = 0
for _ in range(int(input())):
  _input = list(input().rstrip())
  
  for c in _input:
    if c == "A":
      if len(stk) != 0:
        if stk[-1] == "A":
          stk.pop()
        else:
          stk.append("A")
      else:
        stk.append("A")
    elif c == "B":
      if len(stk) != 0:
        if stk[-1] == "B":
          stk.pop()
        else:
          stk.append("B")
      else:
        stk.append("B")
  
  if len(stk) == 0:
    count += 1
    
  stk.clear()

print(count)