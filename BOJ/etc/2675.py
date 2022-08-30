size = int(input())

for i in range(0, size):
  repeat_num, word = input().split()

  result = ""
  for i in range(0, len(word)):
    result += word[i] * int(repeat_num)
  print(result)