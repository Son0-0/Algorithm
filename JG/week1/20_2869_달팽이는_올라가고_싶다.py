a, b, v = map(int, input().split())

x = (v-a)/(a-b)
if (x - int(x)) > 0:
  print(int(x) + 2)
else:
  print(int(x) + 1)