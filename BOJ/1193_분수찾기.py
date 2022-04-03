x = int(input())

if x == 1:
  print("1/1")
else:
  for i in range(1, x+1):
    if i*(i+1) >= 2*x:
      group_num = i
      
      m = int(x - (i*(i-1)/2))
      s = int(group_num - m + 1)
      
      if (group_num % 2) != 0:  
        print(f"{s}/{m}")
      else:
        print(f"{m}/{s}")
        
      break