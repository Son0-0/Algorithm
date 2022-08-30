import sys

pnum = []

def eratos():
	global pnum

	pnum = [num for num in range(1000001)]
	pnum[1] = 0

	for idx in range(1000001):
		if pnum[idx] != 0:
			for i in range(idx*2, 1000001, pnum[idx]):
				pnum[i] = 0
	pnum[2] = 0

def solution():
	eratos()
	while True:
		_input = int(sys.stdin.readline())
		
		if _input == 0:
			break

		result = ""
		for x in range(3, _input+1):
			if pnum[x] != 0 and pnum[(_input - pnum[x])] != 0:
				result = str(_input) + " = " + str(x) + " + " + str(_input - x)
				print(result)
				break

		if len(result) == 0:
			print("Goldbach's conjecture is wrong.")

solution()

# 시간 초과 난 이유: 29 라인에 pnum.count(y) != 0 썼기 때문에
# pnum 소팅, 자르지 말고 그대로 쓰기

# pnum 에서 하나씩 뽑아와서 -> _input 에서 뺀 수가 pnum에 있는지 확인. 있다면 min_value 비교 후 대입
# for x in pnum:
# 	if x > _input:
# 		break
# 	y = _input - x
# 	if pnum[y] != 0: 
# 		result = str(_input) + " = " + str(x) + " + " + str(y)
# 		break
# if len(result) > 0:
# 	print(result)
# else:
# 	print("Goldbach's conjecture is wrong.")