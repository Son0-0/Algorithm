target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]
sorted_list = [0 for _ in range(len(target))]


def merge(left, mid, right):
    i, j, k = left, mid + 1, left

    while i <= mid and j <= right:
        if target[i] <= target[j]:
            sorted_list[k] = target[i]
            i += 1
        else:
            sorted_list[k] = target[j]
            j += 1
        k += 1

    if mid < i:
        for t in range(j, right + 1):
            sorted_list[k] = target[t]
            k += 1
    else:
        for t in range(i, mid + 1):
            sorted_list[k] = target[t]
            k += 1

    for idx in range(left, right + 1):
        target[idx] = sorted_list[idx]


def merge_sort(left, right):
    if left != right:
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        merge(left, mid, right)


print('before:\t', target)
merge_sort(0, len(target) - 1)
print('after:\t', target)
