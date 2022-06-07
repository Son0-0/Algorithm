num = int(input())

if num < 100:
  print(num)
else:
  count = 99
  for i in range(100, num + 1):
    i = str(i)
    
    if i == 1000:
      pass
    else:
      if (int(i[0]) - int(i[1])) == (int(i[1]) - int(i[2])):
        count += 1
  
  print(count)