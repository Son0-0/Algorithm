for t in range(1, int(input()) + 1):
    answer = []

    l, r, _ = map(str, input().split())
    num_list = list(map(str, input().split()))
    ll, rl = len(l), len(r)

    for num in num_list:
        flag = False
        nl = len(num)
        lt, rt = l[:nl], r[:nl+rl-ll]

        for i in range(rl - ll + 1):
            if int(lt) <= int(num) * (10 ** i) <= int(rt):
                flag = True
                break

        if flag:
            answer.append('O')
        else:
            answer.append('X')

    print(f'#{t} ', *answer, sep='')
