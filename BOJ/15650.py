import sys

n, m = map(int, sys.stdin.readline().split())
num_list = [num for num in range(1, n+1)]
result = []

def recur(start, visited, length, rs):
	if length == 0:
		global result
		result.append(rs[:-1])
		return

	for i in range(start, len(visited)):
		if visited[i] == 0:
			visited[i] = 1
			recur(i, visited, length - 1, rs + str(num_list[i]) + " ")
			visited[i] = 0

def solution():
	visited = [0 for _ in range(n)]
	recur(0, visited, m, "")
	result.sort()
	print(*result, sep="\n")

solution()