size = int(input())

for i in range(0, size):
  quiz = input()
  O = quiz.split('X')
  sum = 0

  for score in O:
    current_score = (len(score) * (len(score) + 1)) // 2
    sum += current_score

  print(sum)