import sys

input = sys.stdin.readline
case = int(input())

for _ in range(case):
  num_size = int(input())
  num_list = [num for num in list(map(int, input().split()))]
  
  num_dict = dict()
  
  for num in num_list:
    if num in num_dict:
      num_dict[num] += 1
    else:
      num_dict[num] = 1
      
  cnum_size = int(input())
  cnum_list = [num for num in list(map(int, input().split()))]
  
  for cnum in cnum_list:
    if num_dict.get(cnum) == None:
      print(0)
    else:
      print(1)
      
  num_dict.clear()


# def bin_search(left, right, target):
  
# def solution():
#   for _ in range(case):
#     num_size = int(input())
#     num_list = [num for num in list(map(int, input().split()))]
#     num_list.sort()
    
#     cnum_size = int(input())
#     cnum_list = [num for num in list(map(int, input().split()))]
    
#     for i in 
    
    