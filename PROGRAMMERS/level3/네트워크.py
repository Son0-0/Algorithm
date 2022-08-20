def solution(n, computers):
    answer = 0

    visited = [0 for _ in range(n)]

    def dfs(cur):
        for i in range(n):
            if computers[cur][i] == 1:
                if visited[i] == 0:
                    visited[i] = 1
                    dfs(i)

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
