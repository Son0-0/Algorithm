# 3 2
# 1 2
# 3 4
# 5 6
# 2 3
# -1 -2 0
# 0 0 3

import sys

A = []
B = []

n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
	A.append(list(map(int, sys.stdin.readline().split())))

m, k = map(int, sys.stdin.readline().split())

for _ in range(m):
	B.append(list(map(int, sys.stdin.readline().split())))

def solution():
	result = [[0 for _ in range(k)] for _ in range(n)]
	# result = [[0] * n] * k

	for i in range(n): # 0 1 2
		for kk in range(k): # 0 1 2
			for j in range(m): # 0 1
				result[i][kk] += A[i][j] * B[j][kk]


	for num in result:
		print(*num, sep=" ")

solution()