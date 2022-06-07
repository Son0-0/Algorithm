import sys

size = int(sys.stdin.readline())

llist = [""] * 51
for _ in range(size):
  word = sys.stdin.readline().rstrip()
  llist[len(word)] += word + " "
  
for word in llist:
  if len(word) != 0:
    temp = list(word.split(" "))
    temp = list(set(temp))
    temp.sort()
    
    for i in range(len(temp)):
      if temp[i] != '':
        print(temp[i])