import sys


def solution(rows, columns, queries):
    answer = []

    num_list = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]

    num = 1
    for row in range(1, rows + 1):
        for col in range(1, columns + 1):
            num_list[row][col] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        start = num_list[x1][y1]
        min_value = start

        for i in range(x1, x2):
            min_value = min(min_value, num_list[i][y1])
            num_list[i][y1] = num_list[i + 1][y1]

        for i in range(y1, y2):
            min_value = min(min_value, num_list[x2][i])
            num_list[x2][i] = num_list[x2][i + 1]

        for i in range(x2, x1, -1):
            min_value = min(min_value, num_list[i][y2])
            num_list[i][y2] = num_list[i - 1][y2]

        for i in range(y2, y1, -1):
            min_value = min(min_value, num_list[x1][i])
            num_list[x1][i] = num_list[x1][i - 1]

        num_list[x1][y1 + 1] = start

        answer.append(min_value)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))
