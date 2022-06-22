import sys

input = sys.stdin.readline


def solution():

    input()
    hidden = input().rstrip()

    for i in range(26):
        hidden = hidden.replace(chr(97 + i), ' ')
        hidden = hidden.replace(chr(65 + i), ' ')
        
    hidden = [int(num) for num in list(hidden.split(' ')) if num != '']
    
    if hidden:
        print(sum(hidden))
    else:
        print(0)

solution()