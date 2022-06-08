import sys

input = sys.stdin.readline

def solution():
  pa = list(input().rstrip())
  
  PPAP = ["P", "P", "A", "P"]
  stack = []
  for idx in range(len(pa)):
    stack.append(pa[idx])
    if 4 <= len(stack) and stack[-4:] == PPAP:
      for _ in range(4):
        stack.pop()
      stack.append("P")

  if len(stack) == 1 and stack[0] == 'P':
    print(*PPAP, sep="")
  else:
    print("NP")
    
solution()