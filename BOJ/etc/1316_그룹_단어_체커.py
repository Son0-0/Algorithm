size = int(input())

count = size
for i in range(0, size):
  word = input()
  
  alpha_list = list(set(word))
  
  for alphabet in alpha_list:
    a_count = word.count(alphabet)

    if a_count > 1:
      index = word.index(alphabet)
      temp_list = word[index:index + a_count]
      if temp_list.count(alphabet) != a_count:
        count -= 1
        break

print(count)