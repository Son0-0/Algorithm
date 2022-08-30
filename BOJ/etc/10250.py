size = int(input())

for i in range(0, size):
  h, w, n = map(int, input().split())
  result = ""
  floor = n % h
  if floor == 0:
    floor = h
    ho = n // h
    if ho < 10:
      result = str(floor) + "0" + str(ho)
    else:
      result = str(floor) + str(ho)
  else:
    ho = n // h + 1
    if ho < 10:
      result = str(floor) + "0" + str(ho)
    else:
      result = str(floor) + str(ho)
      
  print(result)