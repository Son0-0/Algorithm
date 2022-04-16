# import sys
# input = sys.stdin.readline
# count = int(input())
# num = [0] * 1001
# rnum = [1,5,10,50]
# result = []

# def recur(lsum, cnt):
# 	if cnt == 0:
# 		if num[lsum] == 0:
# 			num[lsum] += 1
# 		return

# 	for i in range(4):
# 		recur(lsum+rnum[i],cnt - 1)

# def solution():
# 	visited = [0] * 4
# 	recur(0, count)
# 	print(sum(num))

# solution()
import sys
input = sys.stdin.readline
count = int(input())
num = [0] * 1001
rnum = [1,5,10,50]
result = []

def recur(cur, lsum, cnt):
	if cnt == 0:
		if num[lsum] == 0:
			num[lsum] += 1
		return

	for i in range(4):
		if cur <= i:
			recur(i, lsum+rnum[i],cnt - 1)

def solution():
	visited = [0] * 4
	recur(0, 0, count)
	print(sum(num))

solution()