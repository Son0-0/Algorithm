import sys
input = sys.stdin.readline

kit, loss = map(int, input().split())
gain = [num - loss for num in list(map(int, input().split()))]

result = 0

def recur(visited, count, w):
	if w < 500:
		return

	if count == 0:
		global result
		result += 1
		return

	for i in range(kit):
		if visited[i] == 0:
			visited[i] = 1
			recur(visited, count - 1, w+gain[i])
			visited[i] = 0

def solution():
	visited = [0] * kit
	recur(visited, kit, 500)
	print(result)

solution()