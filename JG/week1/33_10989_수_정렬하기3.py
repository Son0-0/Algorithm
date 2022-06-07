import sys

N = int(input())

llist = [0] * 10001
for _ in range(N):
  llist[int(sys.stdin.readline())] += 1

for i in range(1, len(llist)):
  if llist[i] != 0:
    for _ in range(llist[i]):
      print(i)