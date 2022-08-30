a, b, price = map(int, input().split())

income = price - b
if income > 0:
  print(a // income + 1)
else:
  print(-1)