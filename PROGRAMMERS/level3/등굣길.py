def solution(m, n, puddles):
    _map = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    _map[1][1] = 1

    for p in puddles:
        _map[p[1]][p[0]] = -1

    dx, dy = [0, -1], [-1, 0]

    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if _map[row][col] != -1:
                for i in range(2):
                    nx, ny = row + dx[i], col + dy[i]
                    if 1 <= nx <= n and 1 <= ny <= m and _map[nx][ny] != -1:
                        _map[row][col] += _map[nx][ny]

    return _map[n][m] % 1000000007


print(solution(4, 3, [[2, 2]]))
