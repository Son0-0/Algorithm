import sys
input = sys.stdin.readline

size = int(input())
num_list = [num for num in list(map(int, input().split()))]
num_list.sort()

num_dict = dict()
for num in num_list:
  if num in num_dict:
    num_dict[num] += 1
  else:
    num_dict[num] = 1

csize = int(input())
cnum_list = [num for num in list(map(int, input().split()))]

result = []
def bin_search(left, right, target):
  global result
  
  if right < left:
    print(0, end=" ")
    return
  
  mid = (left + right) // 2
  
  mid_num = num_list[mid]
  if mid_num == target:
    fnum = num_dict.get(target)
    print(fnum, end=" ")
    return
  elif mid_num < target:
    return bin_search(mid + 1, right, target)
  else:
    return bin_search(left, mid - 1, target)

def solution():
  global result
  
  for idx in range(csize):
    bin_search(0, size - 1, cnum_list[idx])
  
solution()