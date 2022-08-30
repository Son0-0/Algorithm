def solution():
  self_num = [True] * 10001
  
  for i in range(1, 10000):
    index = is_generate(i)
    self_num[index] = False
    
  for i in range(1, 10001):
    if self_num[i] == True:
      print(i)
    
def is_generate(num: int) -> int:
  generated_num = num
  calc_num = str(num)
  
  for i in range(0, len(calc_num)):
    generated_num += int(calc_num[i])
    
  if generated_num > 10000:
    return 0
  
  return generated_num

solution()