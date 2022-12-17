import sys
from collections import defaultdict

sys = sys.stdin.readline

n, m = map(int, input().split())

ice = defaultdict(set)

for _ in range(m):
    s, d = map(int, input().split())
    ice[s].add(d)
    ice[d].add(s)


def solution():
    
    result = 0

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if j not in ice[i] and k not in ice[i] and k not in ice[j]:
                    result += 1
            

    print(result)


solution()

# import sys

# sys = sys.stdin.readline

# n, m = map(int, input().split())

# wack = set()


# def factorial(num):
#     result = 1
    
#     for i in range(1, num + 1):
#         result *= i
        
#     return result

# def solution():

#     for _ in range(m):
#         temp = list(map(int, input().split()))
        
#         for i in range(1, n + 1):
#             if i not in temp:
#                 wack.add(tuple(sorted(temp + [i])))

#     target = int(factorial(n) / (factorial(n - 3) * factorial(6)))
#     print(target - len(wack))
    
# solution()