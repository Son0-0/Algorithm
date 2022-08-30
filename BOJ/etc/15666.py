import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [int(num) for num in input().split()]
result = []
num_list.sort()

def recur(cur, length, rs):
	if length == 0:
		global result
		if rs[:-1] not in result:
			result.append(rs[:-1])
		return

	for i in range(n):
		if num_list[cur] <= num_list[i]:
			recur(i, length - 1, rs + str(num_list[i]) + " ")

def solution():
	recur(0, m, "")
	print(*result, sep="\n")

solution()