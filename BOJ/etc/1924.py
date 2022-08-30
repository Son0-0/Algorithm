import sys
input = sys.stdin.readline

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

m, d = map(int, input().split())

def solution():
  dday = d
  for i in range(m - 1):
    dday += month[i]
  
  print(day[dday % 7])
  
solution()