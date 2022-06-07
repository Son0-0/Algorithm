import sys

size = int(sys.stdin.readline())

star = "*"
for i in range(1, size + 1):
  temp_str = star * i
  print(temp_str)