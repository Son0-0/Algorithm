import sys

input = sys.stdin.readline

_input = input()


def getSA(data):
  t = 1
  
  size = len(data)
  SA = {}
  GA = {}
  TG = {}
  for i in range(size):
    SA[i] = i
    GA[i] = ord(data[i]) - 65

  while t <= size:
    GA[size] = -1;
    SA.sort()
    
  
  
def solution():
  getSA(_input)
  
solution()