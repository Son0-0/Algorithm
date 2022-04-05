import sys

def gcd(a, b):
	r = a % b
	if r == 0:
		return b
	else:
		return gcd(b,r)

def solution():
	for _ in range(int(sys.stdin.readline())):
		a, b = map(int, sys.stdin.readline().split())
		if a > b:
			print((a*b)//gcd(a,b))
		else:
			print((a*b)//gcd(b,a))

solution()