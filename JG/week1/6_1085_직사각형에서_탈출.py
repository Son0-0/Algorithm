import sys

num_list = list(map(int, sys.stdin.readline().split()))

num_list[2] = num_list[2] - num_list[0]
num_list[3] = num_list[3] - num_list[1]

print(min(num_list))