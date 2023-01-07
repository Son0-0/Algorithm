for c in range(1, int(input())+1):
    r = 0
    for num in list(map(int, input().split())):
        if num % 2 == 1:
            r += num
            
    print(f'#{c}', r)