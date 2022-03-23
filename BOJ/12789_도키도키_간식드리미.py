import sys

input = sys.stdin.readline

size = int(input())
num = [n for n in list(map(int, input().split()))]
num = num[::-1]
stk = []
idx = 1

while len(num) != 0:
  target = num.pop()
  if target != idx:
    if len(stk) != 0 and stk[-1] == idx:
      stk.pop()
      idx += 1
      num.append(target)
    else:
      stk.append(target)
  else:
    idx += 1

result = "Nice"
for _ in range(len(stk)):
  if stk.pop() == idx:
    idx += 1
  else:
    result = "Sad"
    break
    
print(result)