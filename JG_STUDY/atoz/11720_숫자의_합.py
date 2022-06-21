import sys

input = sys.stdin.readline

def solution():
  int(input())
  print(sum(list(map(int, input().strip()))))
  
solution()