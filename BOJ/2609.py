import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(a, b):
	r = a % b
	if r == 0:
		return b
	else:
		return gcd(b, r)

def solution():
	if a > b:
		result = gcd(a, b)
		print(result)
		print((a*b)//result)
	else:
		result = gcd(b, a)
		print(result)
		print((a*b)//result)

solution()