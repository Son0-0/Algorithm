import sys

input = sys.stdin.readline

N, K = map(int, input().split())
word_list = ['anta', 'tica']
_input = ''

for i in range(N):
  word = input().strip()
  word = word.replace('anta', '')
  word = word.replace('tica', '')
  _input += word

def solution():
  print(*_input)
  
solution()