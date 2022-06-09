import sys
from collections import deque

input = sys.stdin.readline
size = int(input())
nqueue = deque(num for num in range(1, size + 1))

for _ in range(size - 1):
  nqueue.popleft()
  nqueue.append(nqueue.popleft())

print(nqueue[-1])

# import sys
# from collections import deque

# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

# N = int(input())

# queue = deque(num for num in range(1, N + 1))

# if N == 1:
#   print(queue.popleft())
# else:
#   while queue:
#     data = queue.popleft()
#     if queue:
#       queue.append(queue.popleft())
#     else:
#       print(data)