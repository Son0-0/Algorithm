number = input()

time = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]

result = 0
for i in range(0, len(number)):
  result += time[ord(number[i]) - 65]
  
print(result)