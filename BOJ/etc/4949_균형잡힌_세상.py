import sys

input = sys.stdin.readline

while True:
  stk = []
  stc = input().rstrip()
  
  if stc == '.':
    break
  else:
    for c in stc:
      if len(stk) == 0 and (c == ')' or c == ']'):
        stk.append(c)
        break
      
      if c == '(' or c =='[':
        stk.append(c)
      elif c == ')':
        if stk[-1] == '(':
          stk.pop()
        else:
          break
      elif c == ']':
        if stk[-1] == '[':
          stk.pop()
        else:
          break
        
    if len(stk) == 0:
      print("yes")
    else:
      print("no")