import sys

size = int(sys.stdin.readline())

llist = list(map(int, sys.stdin.readline().split()))
llist.sort()

print(llist[0]*llist[-1])