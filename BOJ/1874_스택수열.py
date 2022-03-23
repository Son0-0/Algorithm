import sys
input = sys.stdin.readline

size = int(input())
num = [num for num in range(1, size+1)]

push_cnt = 1
stk = []
result = []
for _ in range(size):
  target = int(input())
  while push_cnt <= target:
    stk.append(push_cnt)
    result.append("+")
    push_cnt += 1
  
  if stk[-1] == target:
    stk.pop()
    result.append("-")
  else:
    result.append("NO")

if result.count("NO") != 0:
  print("NO")
else:
  print(*result, sep="\n")