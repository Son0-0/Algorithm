def solution(numbers):
    answer = str(int(''.join(sorted([str(num) for num in numbers],
                                    key=lambda x: x * 3, reverse=True))))
    return '0' if answer[0] == '0' else answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
