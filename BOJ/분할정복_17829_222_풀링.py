import sys

input = sys.stdin.readline

size = int(input())
llist = [list(map(int, input().split())) for _ in range(size)]

def dq(_map, size):
  if size == 2:
    num = []
    for row in range(2):
      for col in range(2):
        num.append(_map[row][col])
    num.sort()
    return num[-2]
  else:
    half = size // 2
    
    pp1 = [p[0:half] for p in _map[0:half]]
    pp2 = [p[half:size] for p in _map[0:half]]
    pp3 = [p[0:half] for p in _map[half:size]]
    pp4 = [p[half:size] for p in _map[half:size]]
    
    temp = [dq(pp1, half), dq(pp2, half), dq(pp3, half), dq(pp4, half)]
    temp.sort()

    return temp[-2]

print(dq(llist, size))

# import sys

# input = sys.stdin.readline

# size = int(input())
# llist = [list(map(int, input().split())) for _ in range(size)]

# def dq(_map, size):
#   if size == 2:
#     num = []
#     for row in range(2):
#       for col in range(2):
#         num.append(_map[row][col])
#     num.sort()
#     return num[-2]
#   else:
#     half = size // 2
    
#     temp = []
    
#     pp1 = [p[0:half] for p in _map[0:half]]
#     pp2 = [p[half:size] for p in _map[0:half]]
#     pp3 = [p[0:half] for p in _map[half:size]]
#     pp4 = [p[half:size] for p in _map[half:size]]
    
#     data1 = dq(pp1, half)
#     if type(data1) == int:
#       temp.append(data1)
#     else:
#       data1.sort()
#       temp.append(data1[-2])
      
#     data2 = dq(pp2, half)
#     if type(data2) == int:
#       temp.append(data2)
#     else:
#       data2.sort()
#       temp.append(data2[-2])
    
#     data3 = dq(pp3, half)
#     if type(data3) == int:
#       temp.append(data3)
#     else:
#       data2.sort()
#       temp.append(data3[-2])     
      
#     data4 = dq(pp4, half)
#     if type(data4) == int:
#       temp.append(data4)
#     else:
#       data4.sort()
#       temp.append(data4[-2])
    
#     if type(temp) == int:
#       return temp
#     else:
#       temp.sort()
#       return temp[-2]

# temp = dq(llist, size)
# if type(temp) == int:
#   print(temp)
# else:
#   temp.sort()
#   print(temp[-2])