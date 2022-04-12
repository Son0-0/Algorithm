import sys

_input = int(sys.stdin.readline())

div = 2
while _input != 1:
	if (_input%div) == 0:
		_input = _input // div
		print(div)
	else:
		div += 1