target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]


def bubble_sort(target):

    for i in range(len(target) - 1):
        for j in range(len(target) - i - 1):
            if target[j + 1] < target[j]:
                target[j], target[j + 1] = target[j + 1], target[j]

        print(f'{i}번째 시도: ', *target)

    print("===")
    print('결과: ', *target)
    print("===")


bubble_sort(target)
