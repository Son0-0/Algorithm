import sys

llist = []
for _ in range(9):
  llist.append(int(input()))
llist.sort()

def solution():
  result = []
  for i in range(0, 8):
    for k in range(1, 9):
      if (sum(llist) - llist[i] - llist[k]) == 100:
        llist.remove(llist[i])
        llist.remove(llist[k-1])
        return

solution()
print(*llist, sep="\n")