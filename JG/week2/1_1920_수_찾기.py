import sys

input = sys.stdin.readline

input_size = int(input())
num_list = [num for num in list(map(int, input().split()))]
num_list.sort()

search_size = int(input())
search_num_list = [num for num in list(map(int, input().split()))]

def binSearch(left, right, target_num):
  if right < left:
    return

  mid = (left + right) // 2
  
  if num_list[mid] == target_num:
    return True
  elif num_list[mid] > target_num:
    return binSearch(left, mid - 1, target_num)
  else:
    return binSearch(mid + 1, right, target_num)
    

def solution():
  for num in search_num_list:
    if binSearch(0, input_size - 1, num) == True:
      print(1)
    else:
      print(0)
      
solution()