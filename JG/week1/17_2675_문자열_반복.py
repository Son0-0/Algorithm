size = int(input())

for case in range(0, size):
  R, S = list(map(str, input().split()))
  
  P = ""
  for i in range(0, len(S)):
    P += S[i] * int(R)
  print(P)