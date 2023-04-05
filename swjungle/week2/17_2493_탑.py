import sys

input = sys.stdin.readline

size = int(input())
llist = [num for num in list(map(int, input().split()))]
result = [0] * len(llist)
stk = []

for i in range(len(llist)):
  while stk:
    if stk[-1][1] > llist[i]:
      result[i] = stk[-1][0] + 1
      break
    else:
      stk.pop()
    
  stk.append([i, llist[i]])

print(*result, sep=" ")