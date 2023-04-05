import sys

N = int(input())

llist = []
for _ in range(N):
  llist.append(int(sys.stdin.readline()))
  
llist.sort()
# for num in llist:
#   print(num)

print(*llist, sep="\n") # list 전체 출력