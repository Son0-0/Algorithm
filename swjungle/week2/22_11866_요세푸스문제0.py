import sys
from collections import deque

n, k = map(int, input().split())
num = deque(num for num in range(1, n + 1))

result = "<"
while num:
  for _ in range(k - 1):
    num.append(num.popleft())
  result += str(num.popleft()) + ", "

result = result[:-2] + ">"
print(result)