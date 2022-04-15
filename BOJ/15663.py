import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [int(num) for num in input().split()]
result = []
num_list.sort()

def recur(visited, length, rs):
	if length == 0:
		global result
		if rs[:-1] not in result:
			result.append(rs[:-1])
		return

	for i in range(n):
		if visited[i] == 0:
			visited[i] = 1
			recur(visited, length - 1, rs + str(num_list[i]) + " ")
			visited[i] = 0

def solution():
	global result
	visited = [0] * n
	recur(visited, m, "")
	print(*result, sep="\n")

solution()