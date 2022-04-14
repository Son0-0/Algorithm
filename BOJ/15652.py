import sys

n, m = map(int, sys.stdin.readline().split())
num_list = [num for num in range(1, n+1)]
result = []

def recur(cur, length, rs):
	if length == 0:
		global result
		result.append(rs[:-1])
		return

	for i in range(n):
		if num_list[cur] <= num_list[i]:
			recur(i, length - 1, rs + str(num_list[i]) + " ")

def solution():
	recur(0, m, "")
	result.sort()
	print(*result, sep="\n")

solution()