import sys

input = sys.stdin.readline


def solution():

    for _ in range(int(input())):
        N = int(input())
        coins = list(map(int, input().split()))
        target = int(input())

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for coin in coins:
            for cur in range(coin, target + 1):
                dp[cur] += dp[cur - coin]

        print(dp[target])

    return 0


solution()
