num1 = int(input())
num2 = input()

for digit in num2[::-1]:
  print(num1 * int(digit))
print(num1 * int(num2))