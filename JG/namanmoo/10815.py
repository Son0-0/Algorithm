# https://www.acmicpc.net/problem/10815

import sys

input = sys.stdin.readline

def solution():
  
  num_dict = {}
  
  N = int(input())
  for num in list(map(int, input().split())):
    num_dict[num] = 1 
  
  N = int(input())
  for num in list(map(int, input().split())):
    if num in num_dict:
      print(1, end=' ')
    else:
      print(0, end=' ')

solution()