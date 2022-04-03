word = input().upper()

alpha_list = list(set(word))
count_list = [0] * 26

for i in range(0, len(alpha_list)):
  count_list[ord(alpha_list[i]) - 65] = word.count(alpha_list[i])
  
result = max(count_list)

if count_list.count(result) > 1:
  print("?")
else:
  print(chr(count_list.index(result) + 65))