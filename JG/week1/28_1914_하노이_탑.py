def move(f, t):
  print(f"{f} {t}")
  
def hanoi(n, f, t, v): # a,c,b
  if n == 1:
    move(f, t)
  else:
    hanoi(n-1,f,v,t) #a,b,c
    move(f,t)
    hanoi(n-1,v,t,f) #b,c,a

def solve():
  size = int(input())
  print(2**size - 1)
  if size <= 20:
    hanoi(size, 1, 3, 2)
  
solve()