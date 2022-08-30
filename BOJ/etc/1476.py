import sys

e, s, m = map(int, sys.stdin.readline().split())

x = 1
while True:
	if (x-e)%15 == 0 and (x-s)%28 == 0 and (x-m)%19 == 0:
		print(x)
		break
	x += 1