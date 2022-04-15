import sys

input = sys.stdin.readline

n = int(input())
num = [int(n) for n in input().split()]

result = []

min_value = sys.maxsize
max_value = -sys.maxsize -1

def calc(odr_list): # 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)
	global min_value, max_value

	sum = num[0]
	for idx in range(n - 1):
		op = odr_list[idx]
		if op == 0:
			sum += num[idx+1]
		elif op == 1:
			sum -= num[idx+1]
		elif op == 2:
			sum *= num[idx+1]
		else:
			# 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다
			if sum < 0:
				sum = -(abs(sum) // num[idx+1])
			else:
				sum = sum // num[idx+1]
	min_value = min(min_value, sum)
	max_value = max(max_value, sum)

def recur(op_count, count, odr_list):
	if count == 0:
		calc(odr_list)
		return

	for i in range(4):
		if op_count[i] != 0:
			op_count[i] -= 1
			odr_list.append(i)
			recur(op_count, count - 1, odr_list)
			odr_list.pop()
			op_count[i] += 1

def solution():
	op_count = [int(n) for n in input().split()]
	recur(op_count, n - 1, [])
	print(max_value)
	print(min_value)

solution()