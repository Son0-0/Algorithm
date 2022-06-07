import sys

tc_size = int(sys.stdin.readline())

for case in range(0, tc_size):
  data = list(map(int, sys.stdin.readline().split()))
  stu_num = data[0]
  score = data[1::]
  
  avg = sum(score) / stu_num
  
  count = 0
  for sc in score:
    if sc > avg:
      count += 1
  result = (count / len(score)) * 100
  print(f"{result:.3f}%")