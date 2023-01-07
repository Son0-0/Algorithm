i=input;t=int(i())
for c in range(1, t+1):
    d=int(i())
    f=list(map(int, i().split()))
    m=f[-1]
    result = 0
    for j in range(d-2,-1,-1):
        if f[j]<m:
            result+=m-f[j]
        else:
            m=f[j]
    print(f'#{c}', result)