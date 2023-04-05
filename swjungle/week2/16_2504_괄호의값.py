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

if stack:
  result = 0
print(result)

# import sys

# input = sys.stdin.readline

# llist = list(input().rstrip())

# stk = []
# for idx in range(len(llist)):
#   if llist[idx] == "(" or llist[idx] == "[":
#     stk.append(llist[idx])
#   elif llist[idx] == ")":
#     if not stk or stk[-1] == "[":
#       stk.append(")")
#       break
#     elif stk[-1] == "(":
#       stk.pop()
#       stk.append(2)
#       continue
#     else:
#       temp = 0
#       while stk[-1] != "(":
#         target = stk.pop()
#         if type(target) != int or len(stk) == 0:
#           temp = 0
#           break
#         temp += target
#       temp *= 2
#       if temp != 0:
#         stk.pop()
#         stk.append(temp)
#   elif llist[idx] == "]":
#     if not stk or stk[-1] == "(":
#       stk.append("]")
#       break
#     elif stk[-1] == "[":
#       stk.pop()
#       stk.append(3)
#       continue
#     else:
#       temp = 0
#       while stk[-1] != "[":
#         target = stk.pop()
#         if type(target) != int or len(stk) == 0:
#           temp = 0
#           break
#         temp += target
#       temp *= 3
#       if temp != 0:
#         stk.pop()
#         stk.append(temp)

# if stk:
#   sum = 0
#   try:
#     for idx in range(len(stk)):
#       if type(idx) == int:
#         sum += int(stk[idx])
#     print(sum)
#   except:
#     print(0)
# else:
#   print(0)