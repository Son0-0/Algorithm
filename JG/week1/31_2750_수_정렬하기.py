N = int(input())

llist = []
for _ in range(N):
  llist.append(int(input()))
  
llist.sort()
for num in llist:
  print(num)