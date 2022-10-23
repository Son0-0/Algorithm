target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]


def insertion_sort(target):

    for i in range(1, len(target)):
        temp = i
        for j in range(i - 1, -1, -1):
            if target[temp] < target[j]:
                target[temp], target[j] = target[j], target[temp]
                temp = j
            else:
                break

        print(f'{i}번째 시도: ', *target)

    print("===")
    print('결과: ', *target)
    print("===")


insertion_sort(target)
