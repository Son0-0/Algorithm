word = input()

alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alphabet in alpha_list:
  word = word.replace(alphabet, '.')

print(len(word))