import sys

min_value = sys.maxsize
_input = int(sys.stdin.readline())

T = (_input//3)

result = []
for i in range(T+1):
	value = _input - (3 * (T - i))
	if (value % 5) == 0:
		min_value = min(min_value, (value//5) + (T-i))

if min_value == sys.maxsize:
	print(-1)
else:
	print(min_value)