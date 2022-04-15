# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# num_list = [int(num) for num in input().split()]
# result = []
# num_list.sort()

# def recur(cur, visited, length, rs):
# 	if length == 0:
# 		global result
# 		if rs[:-1] not in result:
# 			result.append(rs[:-1])
# 		return

# 	for i in range(n):
# 		if visited[i] == 0 and num_list[cur] <= num_list[i]:
# 			visited[i] = 1
# 			recur(i, visited, length - 1, rs + str(num_list[i]) + " ")
# 			visited[i] = 0

# def solution():
# 	global result
# 	visited = [0] * n
# 	recur(0, visited, m, "")
# 	print(*result, sep="\n")

# solution()

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [int(num) for num in input().split()]
result = []
num_list.sort()

def recur(cur, rs):
  if len(rs) == m:
   print(*rs, sep=" ")
   return
 
 for i in range(cur+1, n):
   recur(i, rs + [num_list[i]])

def solution():
	recur(-1, [])

solution()