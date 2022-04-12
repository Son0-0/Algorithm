word = input()
alphabet = [-1] * 26

for alp in word:
  if alphabet[ord(alp) - 97] == -1:
    alphabet[ord(alp) - 97] = word.index(alp)

for a in alphabet:
  print(a, end=" ")