import sys 

input = sys.stdin.readline

llist = [data for data in list(input())]

stk = []
count = 0
for idx in range(len(llist) - 1):
  if llist[idx] == "(":
    stk.append("(")
  else:
    if llist[idx - 1] == "(":
      stk.pop()
      count += len(stk)
    else:
      stk.pop()
      count += 1

print(count)