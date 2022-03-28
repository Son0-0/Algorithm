import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(num for num in range(1, n+1))

result = "<"
while queue:
  for _ in range(k - 1):
    queue.append(queue.popleft())
  result += str(queue.popleft()) + ", "

result = result[:-2] + ">"
print(result)