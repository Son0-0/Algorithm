import sys

while True:
	_input = int(sys.stdin.readline())

	if _input == 0:
		break

	llist = [num for num in range(2 * _input + 1)]
	llist[1] = 0

	for idx in range(len(llist)):
		if llist[idx] != 0:
			for i in range(idx*2, len(llist), llist[idx]):
				llist[i] = 0
	llist = llist[_input+1::]
	print(len(llist) - llist.count(0))