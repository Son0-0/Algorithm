import sys

input = sys.stdin.readline

# (()[[]])([])

stc = list(input().rstrip())

sum = 1
stk = []
num = []
for idx in range(len(stc)):
  if stc[idx] == '(':
    if stc[idx-1] == '(':
      sum *= 2
    stk.append('(')
  elif stc[idx] == ')':
    if stc[idx-1] == '(':

    