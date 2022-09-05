def solution(numbers, hand):
    answer = ''

    key = dict()

    for i in range(1, 10):
        a, b = divmod(i, 3)
        if b == 0:
            b = 2
            a -= 1
        else:
            b -= 1
        key[i] = [a, b]

    key[11] = [3, 0]
    key[0] = [3, 1]
    key[12] = [3, 2]

    left, right = 11, 12
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            lk = abs(key[left][0] - key[num][0]) + \
                abs(key[left][1] - key[num][1])
            rk = abs(key[right][0] - key[num][0]) + \
                abs(key[right][1] - key[num][1])
            if lk < rk:
                answer += 'L'
                left = num
            elif rk < lk:
                answer += 'R'
                right = num
            else:
                if hand == 'right':
                    answer += 'R'
                    right = num
                else:
                    answer += 'L'
                    left = num

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
