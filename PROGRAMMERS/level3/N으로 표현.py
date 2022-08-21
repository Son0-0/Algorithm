def solution(N, number):
    if N == number:
        return 1

    dp = [[] for _ in range(9)]
    dp[0].append(0)
    dp[1].append(N)

    cnt = 2

    while cnt <= 8:
        temp = []
        temp.append(int(str(N) * cnt))
        for i in range(1, cnt // 2 + 1):
            for num1 in dp[cnt - i]:
                for num2 in dp[i]:
                    temp.append(num1 + num2)
                    temp.append(num1 - num2)
                    temp.append(num2 - num1)
                    temp.append(num1 * num2)
                    if num2 != 0:
                        temp.append(num1 // num2)
                    if num1 != 0:
                        temp.append(num2 // num1)
        dp[cnt] = list(set(temp))
        if number in dp[cnt]:
            return cnt
        cnt += 1

    return -1


print(solution(5, 12))
print(solution(2, 11))
print(solution(8, 53))
