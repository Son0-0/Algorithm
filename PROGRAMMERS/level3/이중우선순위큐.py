from heapq import heappop, heappush, heapify


def solution(operations):
    min_heap = []
    max_heap = []

    for operation in operations:
        operand, num = operation.split()
        num = int(num)
        if operand == 'I':
            heappush(max_heap, -num)
            heappush(min_heap, num)
        else:
            if 0 < num:
                if max_heap:
                    heappop(max_heap)
                    temp = []
                    while min_heap:
                        temp.append(heappop(min_heap))
                    temp.pop()
                    heapify(temp)
                    min_heap = temp
            else:
                if min_heap:
                    heappop(min_heap)
                    temp = []
                    while max_heap:
                        temp.append(heappop(max_heap))
                    temp.pop()
                    heapify(temp)
                    max_heap = temp

    size = len(max_heap)
    if size == 0:
        return [0, 0]
    else:
        return [-heappop(max_heap), heappop(min_heap)]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642",
      "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 16"]))
