import sys

input = sys.stdin.readline

llist = list(input().rstrip())

stack = []
temp = 1
result = 0
for idx in range(len(llist)):
  if llist[idx] == "(":
    stack.append("(")
    temp *= 2
  elif llist[idx] == "[":
    stack.append("[")
    temp *= 3
  elif llist[idx] == ")":
    if not stack or stack[-1] == "[":
      result = 0
      break
    
    if stack and llist[idx - 1] == "(":
      result += temp
    stack.pop()
    temp //= 2
  else:
    if not stack or stack[-1] == "(":
      result = 0
      break
    
    if stack and llist[idx - 1] == "[":
      result += temp
    stack.pop()
    temp //= 3

print(result)

# import sys

# input = sys.stdin.readline

# def is_parenthesis(ps):
#   clist = []
#   for _ in range(len(ps)):
#     p = ps.pop()
#     if p == ")":
#       clist.append(")")
#     else:
#       if len(clist) != 0:
#         clist.pop()
#       else:
#         return False
  
#   if len(clist) == 0:
#     return True
#   return False
      
# def solution():
#   for _ in range(int(input())):
#     ps = list(input().rstrip())

#     if is_parenthesis(ps) == True:
#       print("YES")
#       continue
#     print("NO")
    
# solution()