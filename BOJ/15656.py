import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [int(num) for num in input().split()]
result = []
num_list.sort()

def recur(length, rs):
	if length == 0:
		global result
		result.append(rs[:-1])
		return

	for i in range(n):
		recur(length - 1, rs + str(num_list[i]) + " ")


def solution():
	recur(m, "")
	print(*result, sep="\n")

solution()