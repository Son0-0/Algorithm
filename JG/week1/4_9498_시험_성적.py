score = int(input()) // 10 # 1. 입력 받은 정수를 10으로 나눴을 때의 몫을 확인한다.

grade = {
  10: "A",
  9: "A",
  8: "B",
  7: "C",
  6: "D"
}

if score in grade:
  print(grade[score])
else:
  print("F")