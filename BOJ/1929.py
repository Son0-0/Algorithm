import sys

a, b = map(int, sys.stdin.readline().split())

llist = [num for num in range(b+1)]
llist[1] = 0

for index in range(len(llist)):
	if llist[index] != 0:
		for i in range(index*2, len(llist), index):
			llist[i] = 0

for idx in range(a, b+1):
	if llist[idx] != 0:
		print(llist[idx])