import sys

input = sys.stdin.readline

llist = []
for _ in range(int(input())):
  _input = int(input())
  if _input != 0:
    llist.append(_input)
  else:
    llist.pop()
    
print(sum(llist))