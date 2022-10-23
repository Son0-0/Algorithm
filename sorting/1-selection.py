target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]


def selection_sort(target):

    for i in range(len(target)):
        midx, mv = i, target[i]
        for j in range(i + 1, len(target)):
            if target[j] < mv:
                midx, mv = j, target[j]

        target[i], target[midx] = target[midx], target[i]

        print(f'{i}번째 시도: ', *target)

    print("===")
    print('결과: ', *target)
    print("===")


selection_sort(target)
