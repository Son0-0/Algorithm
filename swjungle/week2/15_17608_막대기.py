import sys

input = sys.stdin.readline

llist = []
size = int(input())

for _ in range(size):
  llist.append(int(input()))

slist = [llist.pop()]

for _ in range(size - 1):
  target = llist.pop()
  if slist[-1] < target:
    slist.append(target)
    
print(len(slist))