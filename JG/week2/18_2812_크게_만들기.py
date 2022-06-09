import sys

input = sys.stdin.readline

size, psize = map(int, input().split())
num_list = list(input().rstrip())

stk = []
cnt = 0
for idx in range(0, size):
  while stk and cnt < psize and stk[-1] < num_list[idx]:
    stk.pop()
    cnt += 1

  stk.append(num_list[idx])

print(*stk[:size-psize], sep="")

# import sys

# input = sys.stdin.readline

# n, k = map(int, input().split())
# num = list(input())

# stack = []
# cnt = 0
# for idx in range(n):
#   while stack and cnt < k and stack[-1] < num[idx]:
#     stack.pop()
#     cnt += 1
#   stack.append(num[idx])

# print(*stack[:n-k], sep="")