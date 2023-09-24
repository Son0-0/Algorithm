def maximalSquare(matrix):
    size = len(matrix)

    dp = [[0] * (size + 1) for _ in range(size + 1)]

    max_len = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
                max_len = max(max_len, dp[i + 1][j + 1])

    return max_len


T = int(input())
for tc in range(1, T + 1):
    matrix = []
    for i in range(int(input())):
        matrix.append([0 if item == 1 else 1 for item in list(map(int, input()))])
    print(f"#{tc} {maximalSquare(matrix)}")
