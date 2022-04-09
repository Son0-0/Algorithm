import sys

size = int(sys.stdin.readline())

for i in range(0, size):
  count = 0
  inp = list(map(int, sys.stdin.readline().split()))
  
  stu_size = inp[0] # 학생 수 
  inp = inp[1:] # 학생 점수 list
  inp.sort(reverse=True)
  
  avg = sum(inp) / stu_size
  
  for num in inp:
    if num > avg:
      count += 1
    else:
      break
    
  ratio = (count / stu_size) * 10**2
  print(f"{ratio:.3f}%")