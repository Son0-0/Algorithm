import sys

x, y = map(int, sys.stdin.readline().split())

min_value = sys.maxsize
plate = []
start_point = []


for idx in range(x):
    plate.append(sys.stdin.readline().rstrip())

def check(x, y):
    count_b = 0
    count_w = 0

    for i in range(8):
        for j in range(8):
            target = plate[x+i][y+j]
            if (i % 2) == 0 and (j % 2) == 0: # and target != strt:
                if target != 'B':
                    count_b += 1
                if target != 'W':
                    count_w += 1
            elif (i % 2) == 0 and (j % 2) == 1:
                if target == 'B':
                    count_b += 1
                if target == 'W':
                    count_w += 1
            elif (i % 2) == 1 and (j % 2) == 1:
                if target != 'B':
                    count_b += 1
                if target != 'W':
                    count_w += 1
            elif (i % 2) == 1 and (j % 2) == 0:
                if target == 'B':
                    count_b += 1
                if target == 'W':
                    count_w += 1

    return min(count_b, count_w)

def solution():
    global min_value

    for i in range(x - 7):
        for j in range(y - 7): 
            result = check(i, j)
            min_value = min(result, min_value)

    print(min_value)
solution()