import sys

input = sys.stdin.readline

size = int(input())
pnum = [1,2,3,5,7,9]
result = []

def isPrime(rs):
  target = int(rs)
  for i in range(2, (int(target**0.5))+1):
    if (target % i) == 0:
      return False
    
  return True

def recur(count, rs):
  if rs != "" and isPrime(rs) == False:
    return
  
  if count == 0:
    result.append(int(rs))
    return
  
  for i in range(6):
    if count == size:
      if i == 0 or i == 5:
        continue
    recur(count - 1, rs + str(pnum[i]))
  
def solution():
  recur(size, "")
  print(*result, sep="\n")

solution()