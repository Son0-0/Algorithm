size = int(input())
num = list(map(int, input().split()))

result = 0

for digit in num:
  count = 0
  for i in range(1, digit + 1):
    if (digit % i) == 0:
      count += 1
    if count > 2:
      break
  
  if count == 2:
    result += 1

print(result)