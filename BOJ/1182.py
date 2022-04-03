# import sys

# input = sys.stdin.readline
# size, nsum = map(int, input().split())
# num = [n for n in list(map(int, input().split()))]
# result = 0

# def recur(start, visited, lsum, count):
# 	if count == 0:
# 		global result
# 		if lsum == nsum:
# 			result += 1
# 			return

# 	for i in range(start, size):
# 		if visited[i] == 0:
# 			visited[i] = 1
# 			recur(i, visited, lsum + num[i], count - 1)
# 			visited[i] = 0

# for count in range(size):
# 	visited = [0] * size
# 	recur(0, visited, 0, count + 1)
# print(result)

import sys

input = sys.stdin.readline
size, nsum = map(int, input().split())
num = [n for n in list(map(int, input().split()))]
result = 0

def recur(cur, lsum):
	if cur >= size:
		return

	if (lsum + num[cur]) == nsum:
		global result
		result += 1

	recur(cur+1, lsum)
	recur(cur+1, lsum+num[cur])

def solution():
	recur(0, 0)
	print(result)

solution()