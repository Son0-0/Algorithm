A = int(input())
B = int(input())
C = int(input())

strg = [0] * 10


num = str(A * B * C)
for digit in num:
  strg[int(digit)] += 1
  
for num in strg:
  print(num)