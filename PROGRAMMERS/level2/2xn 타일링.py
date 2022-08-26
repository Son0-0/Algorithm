def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[0], dp[1] = 1, 1

    for idx in range(2, n + 1):
        dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 1000000007

    return dp[n]


print(solution(4))
