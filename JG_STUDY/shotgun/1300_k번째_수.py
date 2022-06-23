import sys

input = sys.stdin.readline

# if n == 3:
# 1 2 3
# 2 4 6
# 3 6 9

# 1 2 2 3 3 4 6 6 9

# if n == 4:
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

# 1 2 2 3 3 4 4 4 6 6 8 8 9 12 12 16

# if n == 5:
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

# 1 2 2 3 3 | 4 4 5 5 5 | 6 6 8 8 9 | 10 10 12 12 15 | 15 16 20 20 25

n = int(input()) 
k = int(input())

def calc(num):
  for num in range(1, num + 1):
    print(num)
    
def binary_search(left, right):
  if right < left:
    return
  
  mid = (left + right) // 2
  

def solution():
  
  target = k // n
  

  return 0
  
solution()