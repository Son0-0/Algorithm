n = int(input())

result = 0
row = [0] * n

def isOk(x):
  for i in range(x):
    if row[i] == row[x] or abs(row[x] - row[i]) == abs(x-i):
      return False
    
  return True
  
def nqueen(x):
  global result
  
  if x == n:
    result += 1
    return
  else:
    for i in range(n):
      row[x] = i
      if isOk(x):
        nqueen(x+1)

nqueen(0)
print(result)