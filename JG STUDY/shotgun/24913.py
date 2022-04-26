import sys, math

input = sys.stdin.readline

# 1번 부터 N번 후보까지 정후는 N+1
N, Q = map(int, input().split())


def solution():
    clist = [0 for _ in range(N + 1)]
    total, jeonghoo_num = 0, 0

    for _ in range(Q):
        a, b, c = map(int, input().split())
        
        if a == 1:
            if c == (N + 1):
                jeonghoo_num += b
            else:
                total += b
                clist[c] += b

        elif a == 2:
            me = jeonghoo_num + b
            
            if me <= max(clist[1:]):
                print("NO")
                continue
            
            if math.ceil((total + c) / N) < me:
                print("YES")
            else:
                print("NO")


solution()