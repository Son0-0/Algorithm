import sys

n, m = map(int, sys.stdin.readline().split())
num_list = [num for num in range(1, n+1)]
result = []

def recur(visited, length, rs):
	if length == 0:
		global result
		result.append(rs[:-1])
		return

	for i in range(len(visited)):
		if visited[i] == 0 and num_list[i] != -1:
			visited[i] = 1
			recur(visited, length - 1, rs + str(num_list[i]) + " ")
			visited[i] = 0

def solution():
	visited = [0 for _ in range(n)]
	recur(visited, m, "")
	result.sort()
	print(*result, sep="\n")

solution()