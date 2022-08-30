import sys
import time

free = int(sys.stdin.readline())

due = []
earn = []
max_value = 0

for _ in range(free):
    a, b = map(int, sys.stdin.readline().split())
    due.append(a)
    earn.append(b)

def recur(cur, pay):
    if cur == free:
        global max_value
        max_value = max(max_value, pay)
        return

    if cur > free:
        return
    recur(cur+1, pay)
    recur(cur+due[cur], pay+earn[cur])

def solution():
    sum = 0
    for idx in range(free):
        recur(idx, 0)
    print(max_value)
 
solution()