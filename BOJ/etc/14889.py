import sys

input = sys.stdin.readline

slist = []
size = int(input())
for _ in range(size):
	slist.append(list(map(int, input().split())))

remain = [num for num in range(len(slist[0]))]
result = sys.maxsize

def calc(team_a):
	global result
	team_b = list(set(remain)-set(team_a))
	score_a = 0
	score_b = 0
	for ia in range(size//2): # 0 1 2
		for ib in range(ia+1,size//2): # 1 2
			score_a += slist[team_a[ia]][team_a[ib]]+slist[team_a[ib]][team_a[ia]]
			score_b += slist[team_b[ia]][team_b[ib]]+slist[team_b[ib]][team_b[ia]]

	result = min(result, abs(score_a-score_b))

def recur(strt, visited, team_list, count):
	if count == 0:
		calc(team_list)
		return

	for i in range(strt, size):
		if visited[i] == 0:
			visited[i] = 1
			team_list.append(i)
			recur(i, visited, team_list, count - 1)
			team_list.pop()
			visited[i] = 0

def solution():
	visited = [0 for num in range(size)]
	team_list = []
	recur(0, visited, team_list, size // 2)
	print(result)

solution()