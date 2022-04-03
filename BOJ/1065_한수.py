def solution():
  size = int(input())

  if size < 100:
    print(size)
  else:
    count = 99

    for i in range(100, size + 1):
      if is_seq(i) == True:
        count += 1
        
    print(count)
  
def is_seq(num: int) -> bool:
  target_num = str(num)
  if (int(target_num[0]) - int(target_num[1])) == (int(target_num[1]) - int(target_num[2])):
    return True
  else:
    return False
  
solution()