def solution(triangle):

    size = len(triangle)
    answer = [[0 for _ in range(i)] for i in range(1, size + 1)]
    answer[0][0] = triangle[0][0]

    for i in range(size - 1):
        for idx, tri in enumerate(triangle[i]):
            answer[i + 1][idx] = max(answer[i + 1][idx],
                                     answer[i][idx] + triangle[i + 1][idx])
            answer[i + 1][idx + 1] = max(answer[i + 1][idx + 1],
                                         answer[i][idx] + triangle[i + 1][idx + 1])

    return max(answer[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
