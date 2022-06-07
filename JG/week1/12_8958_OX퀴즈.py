size = int(input())

for i in range(0, size):
  score = input()
  score = score.split("X")
  result = 0
  for i in score:
    i = len(i)
    result += int((i*(i+1)/2))
  print(result)