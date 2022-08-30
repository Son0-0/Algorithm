target = int(input())

if target == 1:
  print(1)
else:
  for i in range(1, target):
    if (i*(i+1)) > ((target-1)/3):
      if (3*i*(i-1) + 1) == target:
        print(i)
      else:
        print(i+1)
      break