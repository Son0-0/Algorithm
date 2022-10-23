import heapq

target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]


def heap_sort():
    heapq.heapify(target)

    answer = []
    while target:
        answer.append(heapq.heappop(target))

    return answer


print('before:\t', target)
target = heap_sort()
print('after:\t', target)
