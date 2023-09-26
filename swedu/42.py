i,d=input,[0,1,3]
for j in range(3,251): d.append(d[j-1]+d[j-2]*2)
for t in range(1,int(i())+1): print(f'#{t} {d[int(i())]}')