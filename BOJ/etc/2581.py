import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

min_value = sys.maxsize
  
def isPrime(num):
  result = 0  
  for i in range(1, num + 1):
    if (num % i) == 0:
      result += 1
    if result > 2:
      return False
    
  if result == 2:
    return True

def solution():
  result = []
  for num in range(m, n+1):
    if isPrime(num):
      result.append(num)
  
  if sum(result) == 0:
    print(-1)
  else:
    print(sum(result))
    print(min(result))
  
solution()