import sys

t = int(sys.stdin.readline())

def recur(k, n, floor_list):
  temp = []
  _sum = 0
  if k == 0:
    return sum(floor_list)

  for num in floor_list:
    _sum += num
    temp.append(_sum)

  return recur(k - 1, n, temp)

for _ in range(t):
  k = int(sys.stdin.readline()) # 몇층
  n = int(sys.stdin.readline()) # 몇호

  floor_list = [num for num in range(1, n+1)]
  if k < 15 and n < 15:
    print(recur(k - 1, n, floor_list))