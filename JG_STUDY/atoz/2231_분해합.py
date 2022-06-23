import sys

input = sys.stdin.readline

def solution():
  
  _input = int(input().strip())
  input_len = len(str(_input))
  
  strt = _input - 9 * input_len
  strt = 1 * input_len if strt < 0 else strt
  _input = int(_input)
  
  for num in range(strt, _input - 1):
    if num + sum(list(map(int, str(num)))) == _input:
      print(num)
      return
  
  print(0)
  
solution()