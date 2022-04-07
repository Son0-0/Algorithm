# 2
# < > 
import sys

input = sys.stdin.readline

size = int(input())
llist = [d for d in input().split()]
result = [""] * 2
max_value = -sys.maxsize -1
min_value = sys.maxsize

def recur(visited, num, count):
	if 2 <= len(num):
		for i in range(size - count):
			if llist[i] == '<':
				if int(num[i]) >= int(num[i+1]):
					return
			elif llist[i] == '>':
				if int(num[i]) <= int(num[i+1]):
					return

	if count == 0:
		global min_value, max_value
		target = int(num)
		if min_value > target:
			result[1] = num
			min_value = target
		if max_value < target:
			result[0] = num
			max_value = target
		return

	for i in range(10):
		if visited[i] == 0:
			visited[i] = 1
			recur(visited, num + str(i), count - 1)
			visited[i] = 0

def solution():
	visited = [0] * 10
	recur(visited, "", size + 1)
	print(result[0])
	print(result[1])

solution()